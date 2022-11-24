#! /usr/bin/env python

# Copyright IBM Inc. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Authors:
#  Vassilis Vassiliadis

from __future__ import print_function
import sys

total = 0

for num in sys.argv[1:]:
    total += int(num)

print("%d" % total)
