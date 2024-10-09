#! /usr/bin/env python

# Copyright IBM Inc. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Authors:
#  Vassilis Vassiliadis

from __future__ import print_function
import sys
import random

num_rows = int(sys.argv[1])

if len(sys.argv) == 3:
    print("Seeding with %s" % sys.argv[2])
    random.seed(int(sys.argv[2]))

with open('output.csv', 'w') as f:
    for row in range(num_rows):
        line = ' '.join(map(str, [random.randint(0, 10), random.randint(0, 10)]))
        f.write(line + '\n')

print("Generated %d rows" % num_rows)
