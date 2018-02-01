#!/usr/bin/env python

import sys

for line in sys.stdin:
    w = line.strip().split(" ")
    print(w[0] + " " + w[len(w) - 2] + " " + w[len(w) - 1])
