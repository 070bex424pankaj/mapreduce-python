#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    keys = line.split(';')
    date = keys[0]
    value = keys[7]
    print("{};{}".format(date, value))