# 출처: https://www.acmicpc.net/problem/3052

# from sys import stdin

# input = stdin.readline

# rest_li = []

# for _ in range(10):
#     rest = int(input())%42
#     if rest not in rest_li:
#         rest_li.append(rest)
    
# print(len(rest_li))


A = []
for i in range(10):
    A.append((int(input())%42))

b = set(A)

print(len(b))


