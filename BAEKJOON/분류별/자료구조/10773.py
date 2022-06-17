# 출처:https://www.acmicpc.net/problem/10773

from sys import stdin

k = int(stdin.readline())

stack = []

for _ in range(k):
    n = int(stdin.readline())
    if not n == 0:
        stack.append(n)
    else:
        stack.pop()

print(sum(stack))