# 출처:https://www.acmicpc.net/problem/2775

import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    k = int(input())
    n = int(input())
    floor = [i for i in range(1,n+1)]  # 1 2 3 
    new_floor = []
    for a in range(k): # 1
        for i in range(len(floor)): # 2
            new_floor.append(sum(floor[0:i+1]))

        if a != k-1:
            floor = new_floor
            new_floor = []
        else:
            print(new_floor[n-1])

    
    
            