#!/usr/bin/env python3

import hashlib, functools, sys, os


class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def shasum(file):
    with open(file, "rb") as fd:
        hashedfile = hashlib.sha256()
        for buf in iter(functools.partial(fd.read, 128), b''):
            hashedfile.update(buf)
    return hashedfile.hexdigest()


def mdsum(file):
    with open(file, "rb") as fd:
        hashedfile = hashlib.md5()
        for buf in iter(partial(fd.read, 128), b''):
            hashedfile.update(buf)
    return hashedfile.hexdigest()



def main():
    file1 = shasum(sys.argv[1])
    file2 = shasum(sys.argv[2])
    if file1 == file2:
        print(color.OKGREEN + "The files are identical." + color.ENDC)
    else:
        print(color.FAIL + "The file are " + color.BOLD + "not identical." + color.ENDC)

if __name__ == __name__:
    main()
