#!/usr/bin/env python
import sys

last_key = None
max_val = -sys.maxsize-1

for line in sys.stdin:
  # get key and value pair
  key, val = line.split("\t")
  val = int(val) 

  if last_key == key:  # we continue reading same key
    max_val = max(max_val, val) # update maximum

  else:  # we move to a new key (or it is the first read)

    if last_key: # if it is not the first read, print key
       print("%s\t%s" % (last_key, max_val))
    # set new key and initialize maximum 
    last_key = key
    max_val = val

# handling last key (if we ever had one)
if last_key:
  print("%s\t%s" % (last_key, max_val))
