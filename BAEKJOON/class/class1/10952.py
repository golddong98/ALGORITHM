# 출처: https://www.acmicpc.net/problem/10952

import sys

input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a ==0 and b==0:
        break
    sys.stdout.write(f"{a+b}\n")
    
