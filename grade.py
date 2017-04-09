#!/bin/python3


import sys

def solve(grade):
    if grade<38:
        return grade
    if ((grade+2)%5)<(grade%5):
        return (grade+2)-((grade+2)%5)
    return grade


n = int(input().strip())
grades = []
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)

for i in grades:
    print(solve(i))


