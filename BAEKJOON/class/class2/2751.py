# 출처:https://www.acmicpc.net/problem/2751

import sys
input = sys.stdin.readline

raw_result = []

for _ in range(int(input())):
    raw_result.append(int(input()))

sorted_result = sorted(raw_result)

for i in sorted_result:
    print(i)











