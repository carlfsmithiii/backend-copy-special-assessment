#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
# import commands   
import subprocess
import argparse

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', default=os.getcwd(),
                        help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    parser.add_argument('--fromdir', default=os.getcwd(),
                        help='source dir for special files')
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
    special_filenames = get_special_paths(args.fromdir)


def get_special_paths(dir):
    filenames = os.listdir(dir)
    special_filenames = (os.path.join(dir, f)
                         for f in filenames if re.search(r'__\w+__', f))
    return special_filenames


def copy_to(paths, dir):
    for filepath in paths:
        shutil.copy(filepath, dir)



if __name__ == "__main__":
    main()
