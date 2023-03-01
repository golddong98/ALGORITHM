# 출처:https://www.acmicpc.net/problem/1920

# n =int(input())

# n_list = map(int, input().split())

# m = int(input())
# m_list = map(int, input().split())

# n_list = sorted(n_list)

# for el in m_list:
#     s = 0
#     e = len(n_list) -1
#     flag = True
#     while s <= e:
#         m = (s+e)//2
#         if el >n_list[m]:
#             s = m +1
#         elif el < n_list[m]:
#             e = m -1
#         else:
#             print(1)
#             flag = False
#             break
#     if flag:
#         print(0)

from sys import stdin, stdout
# n = stdin.readline()
# N = set(stdin.readline().split())
# m = int(stdin.readline())
# M = stdin.readline().split()

# for l in M:
#     stdout.write('1\n') if l in N else stdout.write('0\n')

n = stdin.readline()
N = sorted(list(map(int,stdin.readline().split())))
m = int(stdin.readline())
M = list(map(int,stdin.readline().split()))

def binary(l, N, start, end):
    if start > end:
        return 0
    mid = (start + end)//2

    if l == N[mid]:
        return 1
    elif l < N[mid]:
        return binary(l, N, start, mid-1)
    else:
        return binary(1, N, mid+1, end)

for l in M:
    start, end = 0, len(N)-1
    print(binary(l, N, start, end))