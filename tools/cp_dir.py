#!/usr/bin/env python3
# Copyright 2012 The Chromium Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Copy a dir.

This module works much like the cp posix command - it takes 2 arguments:
(src, dst) and copies the dir with path |src| to |dst|.
"""

import shutil
import sys


def Main(src, dst):
  try:
    shutil.rmtree(dst)
  except OSError as e:
    if e.errno != 2:  # no such file or directory
      raise e
  shutil.copytree(src, dst)


if __name__ == '__main__':
  Main(sys.argv[1], sys.argv[2])
  sys.exit(0)
