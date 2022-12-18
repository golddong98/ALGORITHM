# 출처: https://www.acmicpc.net/problem/11720

# for _ in range(int(input())):
#     b,*a = map(int, input().split())
#     print(b+sum(a))

import sys

input = sys.stdin.readline

_ = input()

print(sum(map(int, input().rstrip())))
