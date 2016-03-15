# Python 3 program to read an integer from STDIN and output it to STDOUT
import requests

meta_list = []
dict_1 = {}
# Read the variable from STDIN
a = input()
r=requests.get(a)
data = r.text.split('\n')
for i in data:
	data[data.index(i)] =  i.strip(' ')
for i in data:
	if i[0:5] == '<meta':
		meta_list.append(i)
for i in meta_list:
	if 'name=' in i and 'content=' in i:
		dict_1[i.split("\"")[1]] = i.split("\"")[3]
for i in dict_1:
	print(i+">>"+dict_1[i])
# Output the variable to STDOUT
#print(a)
