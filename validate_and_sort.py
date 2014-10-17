#!/usr/bin/env python3
# -.- coding: utf-8 -.-

from os import path
from sys import argv
from yaml import load, dump
from pprint import pprint
BASEDIR = path.abspath(path.dirname(__file__))
qfile = 'queue.yaml'
QUEUE = SITECONF = path.join(BASEDIR, qfile)

def readyaml(filename):
    if path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
            return load(content)

def writeyaml(filename, content):
    with open(filename, 'w') as f:
        f.write(dump(content, indent=4, default_flow_style=False))
    print('#written: %s' %(filename))

if __name__ == '__main__':
    queuec = readyaml(QUEUE)
    pprint(queuec)

    if len(argv) > 1:
        writeyaml(QUEUE, queuec)


