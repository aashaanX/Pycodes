#!/usr/bin/env python
def spend(b,w,x,y,z):
	if x==y and y==z:
		return (b+w)*x
	if x<z and y<z:
		return b*x+w*y
	if x>z and y<z:
		if y+z<x:
			return (b+w)*y+b*z
		else:
			return b*x+w*y
	if x<z and y>z:
		if x+z<y:
			return (b+w)*x+w*z
		else:
			return b*x+w*y
	if x>z and y>z:
		if x>y:
			if y+z<x:
				return (b+w)*y+b*z
			else:
				return b*x+w*y
		else:
			if x+z<y:
				return (b+w)*x+w*z
			else:
				return b*x+w*y



print(spend(212,369,2568,6430,5783))
