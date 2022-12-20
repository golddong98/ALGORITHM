# 출처: https://www.acmicpc.net/problem/1181

import sys

input = sys.stdin.readline

any = []


for _ in range(int(input())):
    word = input().rstrip()
    any.append(word)

result = sorted(set(any), key=lambda x: (len(x),x))

for i in range(len(result)):
    print(result[i])
