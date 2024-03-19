#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys

def main():
  parser = argparse.ArgumentParser(
      description='Script to set environment variables and touch files.')
  parser.add_argument('--stamp', help='Touch stamp file')
  parser.add_argument('--env', nargs=2, action='append',
                      help='Set environment variable')

  args, unknown_args = parser.parse_known_args()

  if args.env:
    for name, value in args.env:
      os.environ[name] = value

  if args.stamp:
    open(args.stamp, 'a').close()

  if unknown_args:
    subprocess.check_call([sys.executable] + unknown_args)

if __name__ == "__main__":
  main()
