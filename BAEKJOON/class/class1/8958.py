# 출처: https://www.acmicpc.net/problem/8958


# for _ in range(int(input())):
#     score = 0
#     result = 0
#     for i in input():
#         if i =='O':
#             score += 1
#         else:
#             score = 0
#         result += score
#     print(result)




import sys

n = int(input())
s =0
for _ in range(n):
    l = sys.stdin.readline().rstrip().split('X')
    for i in range(len(l)):
        s += sum(range(len(l[i])))
    print(s)
    s =0