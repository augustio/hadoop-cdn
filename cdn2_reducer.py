#!/usr/bin/env python

import sys
import collections
import tldextract

counter = collections.Counter()

for line in sys.stdin:
    host, count = line.strip().split(" ", 1)
    ext = tldextract.extract(host)
    if(ext.suffix != ""):
        domain = ext.domain + "." + ext.suffix
    else:
        domain = ext.domain

    counter[domain] += int(count)

for com_domain in counter.most_common(5):
    print(str(com_domain[0]) + " " + str(com_domain[1]))
