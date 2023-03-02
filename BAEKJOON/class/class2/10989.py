# 출처:https://www.acmicpc.net/problem/10989

import sys
input = sys.stdin.readline

results = [0]*10001

for _ in range(int(input())):
    results[int(input())] +=1

for i in range(10001):
    if results[i] != 0:
        for _ in range(results[i]):
            print(i)
