# 출처: https://www.acmicpc.net/problem/1259

import sys

input = sys.stdin.readline

while True:
    p = input().rstrip()

    if p == '0':
        break

    i = 0
    s = 0
    e = len(p)-1 #4-1
    flag = True
    while i < len(p)//2:
        if p[s] != p[e]:
            print('no')
            flag = False
            break
        i += 1
        s += 1
        e -= 1
    if flag:
        print('yes')
    

