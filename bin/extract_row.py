#! /usr/bin/env python

# Copyright IBM Inc. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Authors:
#  Vassilis Vassiliadis


from __future__ import print_function
import sys

file_path = sys.argv[1]
row_idx = int(sys.argv[2])

with open(file_path, 'r') as f:
    for row in range(row_idx):
        f.readline()
    line = f.readline().strip()

if len(line) == 0:
    raise ValueError("Could not fetch row %d from file %s" % (row_idx, file_path))

print(line)