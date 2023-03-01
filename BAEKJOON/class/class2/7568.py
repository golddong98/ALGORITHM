# 출처:https://www.acmicpc.net/problem/7568

import sys

input = sys.stdin.readline

people = []

for _ in range(int(input())):
    people.append(list(map(int,input().rstrip().split())))

cnts = []
for i in range(len(people)):
    cnt = 0
    for j in range(len(people)):
        if (people[i][0] < people[j][0] and people[i][1] < people[j][1]):
            cnt +=1
    cnts.append(cnt+1)

print(*cnts)