#!/usr/bin/env python

import re
import sys

i = 0
for line in sys.stdin:
  # read year
  words = line.split()
  # if temp. is valid and of correct quality, write year & temp
  for word in words:
    print("%s\t%s" % (word, i))
    i++
