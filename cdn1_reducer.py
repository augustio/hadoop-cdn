#!/usr/bin/env python

import sys

cost_per_GB = 0.08 #cents
cost_per_served_request = 0.0009 #cents
bytes_in_GB = 1073741824
served_request_count = 0
data_count = 0
cost = 0
success = 200

for line in sys.stdin:
    host_address, status_code, data_size = line.strip().split(" ", 2)
    if(int(status_code) == success):
        served_request_count += 1
    if(data_size != "-"):
        data_count += float(data_size)
cost = served_request_count * cost_per_served_request + data_count * cost_per_GB / bytes_in_GB
cost = round(cost/100, 2)

print("Number of Served requests: " + str(served_request_count))
print("Size of transferred data: " + str(round(data_count / bytes_in_GB, 4)) + " GB")
print("CDN cost: " + str(cost) + " Euros")
