#!/usr/bin/env python3
# -.- coding: utf-8 -.-

from os import path
from sys import argv
from json import loads, dumps
BASEDIR = path.abspath(path.dirname(__file__))
qfile = 'queue.json'
QUEUE = SITECONF = path.join(BASEDIR, qfile)

def readjson(filename):
    if path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
            return loads(content, strict=False)

def writejson(filename, content):
    with open(filename, 'w') as f:
        f.write(dumps(content, sort_keys=True, indent=2))
    print('#written: %s' %(filename))

if __name__ == '__main__':
    queuec = readjson(QUEUE)

    if len(argv) > 1:
        writejson(QUEUE, list(sorted(queuec)))

    print(
        '''
%s\n%s\n\n%s\n\n
        ''' %(
            qfile, '=' * len(qfile) , queuec
            )
        )
