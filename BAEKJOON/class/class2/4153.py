# 출처:https://www.acmicpc.net/problem/4153

import sys

input = sys.stdin.readline

while True:
    lines = list(map(int,input().rstrip().split()))
    if lines == [0,0,0]:
        break
    lines = sorted(lines)
    if lines[2]**2 == (lines[0]**2 + lines[1]**2):
        print("right")
    else:
        print("wrong")
        