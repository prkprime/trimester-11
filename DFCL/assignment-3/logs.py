#!/usr/bin/env python3

# Author - Pratik Gorade <pratikgorade0@gmail.com>
# Description - analyzing wifi router logs

import csv
import pandas

with open('log.csv', 'r') as log:
    router_log = list(csv.reader(log))[1:]
    count = {}
    for row in router_log:
        if tuple(row) in count.keys():
            count[tuple(row)] += 1
        else:
            count[tuple(row)] = 1

headers = ['Source IP', 'Destination IP', 'Protocol', 'No of Connections']
data = []
for k, v in count.items():
    data.append([*k, v])

df = pandas.DataFrame(data)
df.columns = headers
print(df)