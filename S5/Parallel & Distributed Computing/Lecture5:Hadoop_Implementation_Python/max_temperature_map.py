#!/usr/bin/env python

import re
import sys

for line in sys.stdin:
  # read year
  year = line[15:19]
  # read temperature
  temp = line[87:92]
  # read quality
  q = line[92:93]

  # if temp. is valid and of correct quality, write year & temp
  if (temp != "+9999" and re.match("[01459]", q)):
    print("%s\t%s" % (year, temp))
