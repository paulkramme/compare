#!/usr/bin/env python3

import hashlib
from functools import partial
import sys

def mdsum(file):
    with open(file, "rb") as fd:
        hashedfile = hashlib.md5()
        for buf in iter(partial(fd.read, 128), b''):
            hashedfile.update(buf)
    close(fd)
    return hashedfile.hexdigest()

def main():
    file1 = mdsum(sys.argv[1])
    file2 = mdsum(sys.argv[2])
    if file1 == file2:
        print("The files are identical.")
    else:
        print("The file are NOT identical.")

if __name__ == __name__:
    main()
