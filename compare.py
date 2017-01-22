#!/usr/bin/env python3

import zlib
import hashlib
import functools
import sys
import os


class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def sha256sum(file):
    try:
        with open(file, "rb") as fd:
            hashedfile = hashlib.sha256()
            for buf in iter(functools.partial(fd.read, 128), b''):
                hashedfile.update(buf)
        return hashedfile.hexdigest()
    except FileNotFoundError:
        print(color.WARNING + "The specified file was not found." + color.ENDC)
        return "error"


def sha1sum(file):
    try:
        with open(file, "rb") as fd:
            hashedfile = hashlib.sha1()
            for buf in iter(functools.partial(fd.read, 128), b''):
                hashedfile.update(buf)
        return hashedfile.hexdigest()
    except FileNotFoundError:
        print(color.WARNING + "The specified file was not found." + color.ENDC)
        return "error"


def md5sum(file):
    try:
        with open(file, "rb") as fd:
            hashedfile = hashlib.md5()
            for buf in iter(functools.partial(fd.read, 128), b''):
                hashedfile.update(buf)
        return hashedfile.hexdigest()
    except FileNotFoundError:
        print(color.WARNING + "The specified file was not found." + color.ENDC)
        return "error"
    except PermissionError:
        print(color.WARNING + "Permission denied." + color.ENDC)
        return "permission_denied"


def crc(fileName):
    prev = 0
    for eachLine in open(fileName,"rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X"%(prev & 0xFFFFFFFF)


def main():
    if os.name == "posix":
        file1 = sha256sum(sys.argv[1])
        file2 = sha256sum(sys.argv[2])
        if file1 == file2:
            print(color.OKGREEN + "The files are identical." + color.ENDC)
        else:
            print(color.FAIL + "The file are " + color.BOLD + "not identical." + color.ENDC)
    elif os.name == "nt":
        file1 = shasum(input("Input first path to file: "))
        file2 = shasum(input("Input second path to file: "))
        if file1 == file2:
            print("The files are identical.")
        else:
            print("The files are NOT identical.")
        input("Press ENTER to quit...")
    else:
        print("OS not recognized.")


if __name__ == "__main__":
    main()
