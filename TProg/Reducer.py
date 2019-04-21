#!/usr/bin/python

import sys

(last_key, max_val) = (None, 0)
#initialization

for line in sys.stdin:
	(key, val) = line.strip().split("\t")
	#split year(key) temp(value) using tab delimeter
	if last_key and last_key != key:
		print "%s\t%s" % (last_key, max_val)
		#print max temp of the year
		(last_key, max_val) = (key, val)
		#get next  year and temp
	else:
		(last_key, max_val) = (key, max(max_val, val))
		# get the maximum value for the same year( key)

if last_key:
	print "%s\t%s" % (last_key, max_val)
