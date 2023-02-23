# 출처:https://www.acmicpc.net/problem/10814

import sys

input = sys.stdin.readline

user_list = []


for _ in range(int(input())):
    age, name = input().rstrip().split()
    age = int(age)
    user_list.append((age, name))

results = sorted(user_list, key= lambda x:( x[0]))

for result in results:
    print(result[0],result[1])