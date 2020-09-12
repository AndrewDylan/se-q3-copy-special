#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Andrew Canter"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    directory = os.listdir(dirname)
    specialList = []
    for string in directory:
        if re.search(r'__(\w+)__', string):
            specialList.append(os.path.abspath(os.path.join(dirname, string)))
    return specialList


def copy_to(path_list, dest_dir):
    """Copies list of files to a given directory"""
    fileList = []
    print(path_list)
    if os.path.isdir(dest_dir) is not True:
        os.makedirs(dest_dir)

    for path in path_list:
        if os.path.isdir(path):
            fileList.extend(get_special_paths(path))
        else:
            fileList.append(path)

    for curFile in path_list:
        shutil.copy(curFile, dest_dir)
    return


def zip_to(path_list, dest_zip):
    """Given a list of files, archives them into a given directory"""
    command = "WinRAR a -r " + dest_zip
    commandList = ["WinRAR", "a", "-ep", dest_zip]

    for path in path_list:
        if os.path.isdir(path):
            for files in get_special_paths(path):
                command += " " + files
                commandList.append(files)
        else:
            command += " " + path
            commandList.append(path)

    print("Command I'm going to do:\n" + command)
    subprocess.run(commandList)
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='retrieves special files from dir')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    if ns.from_dir is None:
        exit(1)

    if ns.todir:
        print(ns)
        copy_to(ns.from_dir, ns.todir)
    elif ns.tozip:
        zip_to(ns.from_dir, ns.tozip)
    else:
        absList = get_special_paths(ns.from_dir)
        for path in absList:
            print(path)


if __name__ == "__main__":
    main(sys.argv[1:])
