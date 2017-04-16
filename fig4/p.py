#!/usr/bin/env python
import sys

try:
	filename = sys.argv[1]
except:
	print "Usage:", sys.argv[0], "input file"; sys.exit(1)

ifn = filename + ".txt"
of3 = filename + ".outlet.txt"


ifil1 = open(ifn,'r')
ofil3 = open(of3,'w')

ic  = 0
l1 = ifil1.readline()
l2 = ifil1.readline()
l3 = ifil1.readline()
l4 = ifil1.readline()
l5 = ifil1.readline()
#l5 = ifil1.readline()

for line in ifil1:
        if ic == 0:
                ic = ic + 1
	elif ic == 1:
                ic = ic + 1
	else:
		ofil3.writelines(line)
                ic = 0 
ifil1.close()
ofil3.close()
