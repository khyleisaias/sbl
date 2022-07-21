#!/usr/bin/env python3
from libptsd import *


if __name__ == '__main__':
    file = open("test.txt", 'r')
    printf("%s\n" % file.read())
