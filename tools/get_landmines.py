#!/usr/bin/env python3
# Copyright 2024 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
This file emits the list of reasons why a particular build needs to be clobbered
(or a list of 'landmines').
"""

import os
import sys

sys.path.insert(0, os.path.abspath(
  os.path.join(os.path.dirname(__file__), '..', 'build')))

import get_landmines as build_get_landmines


def print_landmines():  # pylint: disable=invalid-name
  """
  ALL LANDMINES ARE EMITTED FROM HERE.
  """
  # DO NOT add landmines as part of a regular CL. Landmines are a last-effort
  # bandaid fix if a CL that got landed has a build dependency bug and all bots
  # need to be cleaned up. If you're writing a new CL that causes build
  # dependency problems, fix the dependency problems instead of adding a
  # landmine.
  # See the Chromium version in src/build/get_landmines.py for usage examples.
  print('Switch to in-tree GN configsXX.')
  print('Build test with build_addons.py.')
  build_get_landmines.print_landmines()
  return 0


def main():
  print_landmines()
  return 0


if __name__ == '__main__':
  sys.exit(main())
