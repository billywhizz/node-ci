#!/usr/bin/env python3
# Copyright (c) 2013-2019 GitHub Inc.
# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import json
import os
import subprocess
import sys

basedir = os.path.dirname(__file__)
sys.path.append(os.path.join(basedir, os.pardir, 'node', 'tools'))
import install

def LoadPythonDictionary(path):
  file_string = open(path).read()
  try:
    file_data = eval(file_string, {'__builtins__': None}, None)
  except SyntaxError as e:
    e.filename = path
    raise
  except Exception as e:
    raise Exception('Unexpected error while reading %s: %s' % (path, str(e)))

  assert isinstance(file_data, dict), '%s does not eval to a dictionary' % path

  return file_data

def ReplaceVariable(dictionary, var, ignore_list):
  if var in ignore_list:
    return []
  if var.startswith('<@('):
    var_name = var[3:-1]
    assert var_name in dictionary['variables'], \
        'Variable %s not found defined in gyp file' % var_name
    return ReplaceVariables(dictionary,
                            dictionary['variables'][var_name],
                            ignore_list)
  else:
    return [var]

def ReplaceVariables(dictionary, sources, ignore_list = []):
  return [replacement for source in sources
          for replacement in ReplaceVariable(dictionary, source, ignore_list)]

FILENAMES_JSON_HEADER = '''
// This file is automatically generated by generate_gn_filenames_json.py
// DO NOT EDIT
'''.lstrip()

def dedup(a_list):
  return list(set(a_list))

def RedirectV8(list):
  return [f.replace('deps/v8/', '../v8/', 1) for f in list]

def GitLsFiles(path, prefix):
  output = subprocess.check_output(['git', 'ls-files'], cwd=path).decode()
  return [prefix + x for x in output.splitlines()]

def SearchNodeLibraryFiles(node_dir, entry):
  assert(entry == '<@(node_library_files)')
  files = []
  prefix_size = len(node_dir) + 1
  for (dir, _, fs) in os.walk(os.path.join(node_dir,'lib')):
    for f in fs:
      if f.endswith(".js"):
        files.append(os.path.join(dir, f)[prefix_size:])
  return files

def GypExpandList(node_dir, list):
  entries = []
  for entry in list:
    if entry == '<@(node_library_files)':
      entries = entries + SearchNodeLibraryFiles(node_dir, entry)
    else:
      entries.append(entry)
  return entries

if __name__ == '__main__':
  # Set up paths.
  root_dir = os.path.dirname(os.path.dirname(__file__))
  node_dir = os.path.join(root_dir, 'node')
  node_gyp_file = os.path.join(node_dir, 'node.gyp')
  out_file = os.path.join(root_dir, 'node_files.json')
  inspector_gyp_file = os.path.join(node_dir,
      'src', 'inspector', 'node_inspector.gypi')
  openssl_gyp_file = os.path.join(node_dir,
      'deps', 'openssl', 'config', 'archs',
      'linux-x86_64', 'no-asm', 'openssl.gypi')
  nghttp2_gyp_file = os.path.join(node_dir,
      'deps', 'nghttp2', 'nghttp2.gyp')
  cares_gyp_file = os.path.join(node_dir,
      'deps', 'cares', 'cares.gyp')
  base64_gyp_file = os.path.join(node_dir,
      'deps', 'base64', 'base64.gyp')
  out = {}
  # Load file lists from gyp files.
  node_gyp = LoadPythonDictionary(node_gyp_file)
  inspector_gyp = LoadPythonDictionary(inspector_gyp_file)
  openssl_gyp = LoadPythonDictionary(openssl_gyp_file)
  nghttp2_gyp = LoadPythonDictionary(nghttp2_gyp_file)
  cares_gyp = LoadPythonDictionary(cares_gyp_file)
  base64_gyp = LoadPythonDictionary(base64_gyp_file)

  # Find JS lib file and single out files from V8.
  library_files = GypExpandList(node_dir, node_gyp['variables']['library_files'])
  deps_files = node_gyp['variables']['deps_files']
  library_files += deps_files

  # Remove '<@(node_builtin_shareable_builtins)'.
  # We do not support  externally shared js builtins.
  # See: https://github.com/nodejs/node/pull/44376
  # TODO(victorgomes): We need a way to get these externally shareable builtins
  # from configure.py. I have a feeling this is still in flux in the NodeJS side,
  # so let's delay this a bit.
  library_files.remove('<@(node_builtin_shareable_builtins)')
  library_files.remove('<@(linked_module_files)')
  library_files.append('deps/cjs-module-lexer/lexer.js')
  library_files.append('deps/cjs-module-lexer/dist/lexer.js')
  library_files.append('deps/undici/undici.js')

  out['node_library_files'] = [
      f for f in library_files if not f.startswith('deps/v8')]
  out['all_library_files'] = library_files

  # Find C++ source files.
  node_lib_target = next(
      t for t in node_gyp['targets']
      if t['target_name'] == '<(node_lib_target_name)')
  node_source_blacklist = {
      '<@(library_files)',
      '<@(deps_files)',
      'common.gypi',
      '<(SHARED_INTERMEDIATE_DIR)/node_javascript.cc',
      '<@(node_library_files)',
      '<@(node_builtin-shareable_builtins)',
  }
  node_sources = [
      f for f in ReplaceVariables(node_gyp,
                                  node_lib_target['sources'],
                                  node_source_blacklist)
      if f not in node_source_blacklist]
  out['node_sources'] = [
      f.replace('deps/v8/', '../v8/', 1) for f in node_sources]

  # Find C++ sources when building with crypto.
  node_use_openssl = next(
      t for t in node_lib_target['conditions']
      if t[0] == 'node_use_openssl=="true"')
  out['crypto_sources'] = dedup(ReplaceVariables(node_gyp,
                                                 node_use_openssl[1]['sources'])
                                )

  # Find cctest files. Omit included gtest.
  cctest_target = next(
      t for t in node_gyp['targets']
      if t['target_name'] == 'cctest')
  out['cctest_sources'] = [
      f for f in cctest_target['sources'] if not f.startswith('test/cctest/gtest')]

  # Find inspector sources.
  inspector_sources = list(map(lambda s: '../../' + s,
                               ReplaceVariables(inspector_gyp,
                                                inspector_gyp['sources'])
                               ))
  out['inspector_sources'] = inspector_sources

  # Find OpenSSL sources.
  # OpenSSL sources countain duplicate sources, so we remove duplicates by applying list(set())
  openssl_sources = set(openssl_gyp['variables']['openssl_sources'])
  openssl_sources = openssl_sources.union(set(openssl_gyp['variables']['openssl_sources_linux-x86_64']))
  # HACK: Remove libraries from sources
  openssl_sources = {source for source in openssl_sources if not source.endswith('.ld')}
  out['openssl_sources'] = list(openssl_sources)

  # Find nghttp2 sources.
  nghttp2_sources = ReplaceVariables(nghttp2_gyp, nghttp2_gyp['targets'][0]['sources'])
  out['nghttp2_sources'] = nghttp2_sources

  # Find cares sources.
  cares_sources = ReplaceVariables(cares_gyp, cares_gyp['targets'][0]['sources'])
  out['cares_sources'] = cares_sources

  # Find base64 sources.
  base64_sources = ReplaceVariables(base64_gyp, base64_gyp['targets'][0]['sources'])
  out['base64_sources'] = base64_sources

  # Find node/tools/doc content.
  tools_doc_dir = os.path.join(node_dir, 'tools', 'doc')
  out['tools_doc_files'] = GitLsFiles(tools_doc_dir, '//node/tools/doc/')

  # Find node/test/addons content.
  test_addons_dir = os.path.join(node_dir, 'test', 'addons')
  out['test_addons_files'] = GitLsFiles(test_addons_dir, '//node/test/addons/')

  # Find node/test/node-api content.
  test_node_api_dir = os.path.join(node_dir, 'test', 'node-api')
  out['test_node_api_files'] = GitLsFiles(test_node_api_dir,
                                          '//node/test/node-api/')
  # Find node/test/js-native-api content.
  test_js_native_api_dir = os.path.join(node_dir, 'test', 'js-native-api')
  out['test_js_native_api_files'] = GitLsFiles(test_js_native_api_dir,
                                               '//node/test/js-native-api/')

  # Find v8/include content.
  v8_include_dir = os.path.join(root_dir, 'v8', 'include')
  out['v8_headers'] = GitLsFiles(v8_include_dir, '//v8/include/')

  # Write file list as JSON.
  with open(out_file, 'w') as f:
    f.write(FILENAMES_JSON_HEADER)
    f.write(json.dumps(out, sort_keys=True, indent=2, separators=(',', ': ')))
    f.write('\n')
