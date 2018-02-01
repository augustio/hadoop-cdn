#!/usr/bin/env python

import sys

for l in sys.stdin:
    w = l.strip().split(" ")
    print(w[0] + " " + "1")
