# 출처: https://www.acmicpc.net/problem/10951

# import sys
# input = sys.stdin.readline

# while True:
#     try:
#         a,b = map(int, input().split())
#         print(a+b)
#     except EOFError:
#         break

import sys

lines = sys.stdin.readlines()
for line in lines:
    a, b =map(int, line.split())
    print(a+b)





