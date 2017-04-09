#!/bin/python3

def bsearch(sorted_list,key):
    mid = len(sorted_list)//2
    if(sorted_list[mid]==key):
        return True
    elif(sorted_list[mid]<key):
        return bsearch(sorted_list[0:mid-1],key)
    else:
        return bsearch(sorted_list[mid+1:],key)

a = [1,2,3,4,6,7,9,10]

if(bsearch(a,7)):
    print("found")
else:
    print("Not found")
