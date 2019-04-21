#!/usr/bin/python
#used to ensure pyhon code will execute in aboce location

import sys
# inbuilt module to read the file from standard input

for line in sys.stdin:
	val = line.strip()
	#remove leading and trailing spacing
	(year, temp) = (val[0:4], val[5:9])
	#segregate year and temprature

	if(temp != "9999"):
	#used for filtering data
		print "%s\t%s" % (year,temp)
