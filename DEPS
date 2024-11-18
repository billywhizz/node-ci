# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

use_relative_paths = True

gclient_gn_args_file = 'build/config/gclient_args.gni'
gclient_gn_args = [
  'build_upstream_node',
]

vars = {
  # Set to true to use deps bundled in node.
  'build_upstream_node': False,

  'abseil_revision': '16df85f9a7ced865a722e21787a0d96440edc0ab',
  'abseil_url': 'https://chromium.googlesource.com/chromium/src/third_party/abseil-cpp.git',

  'build_revision': '636ceb6dea83e899eb5d168a32c293bf85c3bb5c',
  'build_url': 'https://chromium.googlesource.com/chromium/src/build.git',

  'buildtools_revision': 'd62e23e82180d514dbf1d5d7caffd7dcbc3294c1',
  'buildtools_url': 'https://chromium.googlesource.com/chromium/src/buildtools.git',

  'buildtools_clang_format_revision': '2221d56f57b4346042368e520140e5894d319f94',
  'buildtools_clang_format_url': 'https://chromium.googlesource.com/external/github.com/llvm/llvm-project/clang/tools/clang-format.git',

  'buildtools_libcxx_revision': '2a2315e69ab61cb488c18fbbb1cd502be049c122',
  'buildtools_libcxx_url': 'https://chromium.googlesource.com/external/github.com/llvm/llvm-project/libcxx.git',

  'buildtools_libcxxabi_revision': '0226cb1cdfe740b173394e1cebbd0dcf293e38ad',
  'buildtools_libcxxabi_url': 'https://chromium.googlesource.com/external/github.com/llvm/llvm-project/libcxxabi.git',

  'buildtools_libunwind_revision': '69b8c646978a1650f10ee7c355b85018a3e23909',
  'buildtools_libunwind_url': 'https://chromium.googlesource.com/external/github.com/llvm/llvm-project/libunwind.git',

  'clang_revision': '37d1894d5350b2cdfde3b4a81858c8d14c7c5eb8',
  'clang_url': 'https://chromium.googlesource.com/chromium/src/tools/clang.git',

  'depot_tools_revision': 'b5eb54d5c1aeae79c8b07a516bdf3e380ad0bba7',
  'depot_tools_url': 'https://chromium.googlesource.com/chromium/tools/depot_tools.git',

  # Fetch configuration files required for the 'use_remoteexec' gn arg
  'download_remoteexec_cfg': False,

  # GN CIPD package version.
  'gn_version': 'git_revision:e9e83d9095d3234adf68f3e2866f25daf766d5c7',

  # ninja CIPD package version.
  # https://chrome-infra-packages.appspot.com/p/infra/3pp/tools/ninja
  'ninja_version': 'version:2@1.11.1.chromium.6',

  'fast_float_revision': 'd7417618f93d2c47e9bbde561510f9fc8bafe003',
  'fast_float_url': 'https://chromium.googlesource.com/external/github.com/fastfloat/fast_float.git',

  'fp16_revision': '98b0a46bce017382a6351a19577ec43a715b6835',
  'fp16_url': 'https://chromium.googlesource.com/external/github.com/Maratyszcza/FP16.git',

  'googletest_revision': 'd144031940543e15423a25ae5a8a74141044862f',
  'googletest_url': 'https://chromium.googlesource.com/external/github.com/google/googletest.git',

  'icu_revision': 'c12357a8ce1de15f219db37179b3c72af001610c',
  'icu_url': 'https://chromium.googlesource.com/chromium/deps/icu.git',

  'jinja2_revision': '5e1ee241ab04b38889f8d517f2da8b3df7cfbd9a',
  'jinja2_url': 'https://chromium.googlesource.com/chromium/src/third_party/jinja2.git',

  'markupsafe_revision': '9f8efc8637f847ab1ba984212598e6fb9cf1b3d4',
  'markupsafe_url': 'https://chromium.googlesource.com/chromium/src/third_party/markupsafe.git',

  'node_revision': '0d04c508af1242893b0b5284f68f8222939c1f81',
  'node_url': 'https://chromium.googlesource.com/external/github.com/v8/node.git',

  'trace_common_revision' : '148c806f46c0f8d2e5e888a8175b656ad4cfee43',
  'trace_common_url': 'https://chromium.googlesource.com/chromium/src/base/trace_event/common.git',

  'v8_revision': '5ddcc5462d923efe9aaa36d82fe47b2371f0ce10',
  'v8_url': 'https://chromium.googlesource.com/v8/v8.git',

  'zlib_revision': '82a5fecf8aae8f288267cfdb2d29c9ebf7b37e59',
  'zlib_url': 'https://chromium.googlesource.com/chromium/src/third_party/zlib.git',

  'reclient_version': 're_client_version:0.105.0.d6a0caf-gomaip',

  # RBE instance to use for running remote builds
  'rbe_instance': Str('projects/rbe-chrome-untrusted/instances/default_instance'),

  # RBE project to download rewrapper config files for. Only needed if
  # different from the project used in 'rbe_instance'
  'rewrapper_cfg_project': Str(''),
}

deps = {
  'base/trace_event/common': {
    'url': Var('trace_common_url') + '@' + Var('trace_common_revision'),
    'condition': 'not build_upstream_node',
  },
  'build': Var('build_url') + '@' + Var('build_revision'),
  'buildtools': Var('buildtools_url') + '@' + Var('buildtools_revision'),
  'buildtools/clang_format/script': Var('buildtools_clang_format_url') + '@' + Var('buildtools_clang_format_revision'),
  'third_party/libc++/src': Var('buildtools_libcxx_url') + '@' + Var('buildtools_libcxx_revision'),
  'third_party/libc++abi/src': Var('buildtools_libcxxabi_url') + '@' + Var('buildtools_libcxxabi_revision'),
  'third_party/libunwind/src': Var('buildtools_libunwind_url') + '@' + Var('buildtools_libunwind_revision'),
  'node': Var('node_url') + '@' + Var('node_revision'),
  'third_party/abseil-cpp': Var('abseil_url') + '@' + Var('abseil_revision'),
  'third_party/depot_tools': Var('depot_tools_url') + '@' + Var('depot_tools_revision'),
  'third_party/fast_float/src': Var('fast_float_url') + '@' + Var('fast_float_revision'),
  'third_party/fp16/src': {
    'url': Var('fp16_url') + '@' + Var('fp16_revision'),
    'condition': 'not build_upstream_node',
  },
  'third_party/googletest/src': {
    'url': Var('googletest_url') + '@' + Var('googletest_revision'),
    'condition': 'not build_upstream_node',
  },
  'third_party/icu': Var('icu_url') + '@' + Var('icu_revision'),
  'third_party/jinja2': Var('jinja2_url') + '@' + Var('jinja2_revision'),
  'third_party/markupsafe': Var('markupsafe_url') + '@' + Var('markupsafe_revision'),
  'third_party/zlib': Var('zlib_url') + '@' + Var('zlib_revision'),
  'tools/clang': Var('clang_url') + '@' + Var('clang_revision'),
  'v8': {
    'url': Var('v8_url') + '@' +  Var('v8_revision'),
    'condition': 'not build_upstream_node',
  },
  'buildtools/linux64': {
    'packages': [
      {
        'package': 'gn/gn/linux-${{arch}}',
        'version': Var('gn_version'),
      }
    ],
    'dep_type': 'cipd',
    'condition': 'host_os == "linux"',
  },
  'buildtools/mac': {
    'packages': [
      {
        'package': 'gn/gn/mac-${{arch}}',
        'version': Var('gn_version'),
      }
    ],
    'dep_type': 'cipd',
    'condition': 'host_os == "mac"',
  },
  'buildtools/win': {
    'packages': [
      {
        'package': 'gn/gn/windows-amd64',
        'version': Var('gn_version'),
      }
    ],
    'dep_type': 'cipd',
    'condition': 'host_os == "win"',
  },
  'buildtools/reclient': {
    'packages': [
      {
        'package': 'infra/rbe/client/${{platform}}',
        'version': Var('reclient_version'),
      }
    ],
    'dep_type': 'cipd',
    'condition': '(host_os == "linux" or host_os == "mac" or host_os == "win") and (host_cpu != "arm64" or host_os == "mac")',
  },
  'third_party/ninja': {
    'packages': [
      {
        'package': 'infra/3pp/tools/ninja/${{platform}}',
        'version': Var('ninja_version'),
      }
    ],
    'dep_type': 'cipd',
  },
}

hooks = [
  {
    # This clobbers when necessary (based on get_landmines.py). It must be the
    # first hook so that other things that get/generate into the output
    # directory will not subsequently be clobbered.
    'name': 'landmines',
    'pattern': '.',
    'action': [
        'python3',
        'build/landmines.py',
        '--landmine-scripts',
        'tools/get_landmines.py',
    ],
  },
  {
    # Update the Windows toolchain if necessary.
    'name': 'win_toolchain',
    'pattern': '.',
    'condition': 'checkout_win',
    'action': ['python3', 'build/vs_toolchain.py', 'update'],
  },
  {
    # Update the Mac toolchain if necessary.
    'name': 'mac_toolchain',
    'pattern': '.',
    'condition': 'checkout_mac',
    'action': ['python3', 'build/mac_toolchain.py'],
  },
  {
    'name': 'clang',
    'pattern': '.',
    'action': ['python3', 'tools/clang/scripts/update.py'],
  },
  {
    # Update LASTCHANGE.
    'name': 'lastchange',
    'pattern': '.',
    'action': ['python3', 'build/util/lastchange.py',
               '-o', 'build/util/LASTCHANGE'],
  },
  {
    'name': 'sysroot_arm',
    'pattern': '.',
    'condition': '(checkout_linux and checkout_arm)',
    'action': ['python3',
               'build/linux/sysroot_scripts/install-sysroot.py',
               '--arch=arm'],
  },
  {
    'name': 'sysroot_arm64',
    'pattern': '.',
    'condition': '(checkout_linux and checkout_arm64)',
    'action': ['python3',
               'build/linux/sysroot_scripts/install-sysroot.py',
               '--arch=arm64'],
  },
  {
    'name': 'sysroot_x86',
    'pattern': '.',
    'condition': '(checkout_linux and (checkout_x86 or checkout_x64))',
    'action': ['python3',
               'build/linux/sysroot_scripts/install-sysroot.py',
               '--arch=x86'],
  },
  {
    'name': 'sysroot_x64',
    'pattern': '.',
    'condition': 'checkout_linux and checkout_x64',
    'action': ['python3',
               'build/linux/sysroot_scripts/install-sysroot.py',
               '--arch=x64'],
  },

  # Pull clang-format binaries using checked-in hashes.
  {
    'name': 'clang_format_win',
    'pattern': '.',
    'condition': 'host_os == "win"',
    'action': [ 'python3',
                'third_party/depot_tools/download_from_google_storage.py',
                '--no_resume',
                '--no_auth',
                '--bucket', 'chromium-clang-format',
                '-s', 'buildtools/win/clang-format.exe.sha1',
    ],
  },
  {
    'name': 'clang_format_mac_x64',
    'pattern': '.',
    'condition': 'host_os == "mac" and host_cpu == "x64"',
    'action': [ 'python3',
                'third_party/depot_tools/download_from_google_storage.py',
                '--no_resume',
                '--no_auth',
                '--bucket', 'chromium-clang-format',
                '-s', 'buildtools/mac/clang-format.x64.sha1',
                '-o', 'buildtools/mac/clang-format',
    ],
  },
  {
    'name': 'clang_format_mac_arm64',
    'pattern': '.',
    'condition': 'host_os == "mac" and host_cpu == "arm64"',
    'action': [ 'python3',
                'third_party/depot_tools/download_from_google_storage.py',
                '--no_resume',
                '--no_auth',
                '--bucket', 'chromium-clang-format',
                '-s', 'buildtools/mac/clang-format.arm64.sha1',
                '-o', 'buildtools/mac/clang-format',
    ],
  },
  {
    'name': 'clang_format_linux',
    'pattern': '.',
    'condition': 'host_os == "linux"',
    'action': [ 'python3',
                'third_party/depot_tools/download_from_google_storage.py',
                '--no_resume',
                '--no_auth',
                '--bucket', 'chromium-clang-format',
                '-s', 'buildtools/linux64/clang-format.sha1',
    ],
  },

  # Configure remote exec cfg files
  {
    'name': 'configure_reclient_cfgs',
    'pattern': '.',
    'condition': 'download_remoteexec_cfg',
    'action': ['python3',
               'buildtools/reclient_cfgs/configure_reclient_cfgs.py',
               '--rbe_instance',
               Var('rbe_instance'),
               '--reproxy_cfg_template',
               'reproxy.cfg.template',
               '--rewrapper_cfg_project',
               Var('rewrapper_cfg_project'),
               '--quiet',
               ],
  },
]
