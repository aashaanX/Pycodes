#!/bin/python3
import sys
import string
n = int(input().strip())
s = input().strip()
k = int(input().strip())
ans=''
for i in s:
	if i in string.ascii_lowercase:
		new_char=chr(ord(i)+k%26)
		if (ord(new_char)>ord('z')):
			new_char=chr(ord(new_char)-26)
	elif i in (string.ascii_uppercase):
		new_char=chr(ord(i)+k%26)
		if (ord(new_char)>ord('Z')):
			new_char=chr(ord(new_char)-26)
	else:
		new_char = i
	ans += new_char
print(ans)
