#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

minimum = min(a,b,c,d,e)
maximum = max(a,b,c,d,e)

sum = a+b+c+d+e

print(sum-maximum,sum-minimum)

