# 출처: https://www.acmicpc.net/problem/2742

from sys import stdout

print = stdout.write


for i in range(int(input()),0,-1):
    print(str(i)+'\n')

# for i in range(5, 1, -1):
#     print(str(i))

n = int(input())
print("\n".join(map(str, range(n,0,-1))))






