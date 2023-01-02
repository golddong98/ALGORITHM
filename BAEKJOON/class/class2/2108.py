# 출처:https://www.acmicpc.net/problem/2108

import sys, collections

input = sys.stdin.readline

res = []

for _ in range(int(input())):
    res.append(int(input()))

res1 = round(sum(res)/len(res))
print(res1)

res2 = sorted(res)[len(res)//2]
print(res2)

if len(res) ==1:
    print(res[0])
else:
    c = collections.Counter(res).most_common()
    maximum = c[0][1]
    res3 = []
    for num in c:
        if num[1] == maximum:
            res3.append(num[0])
    if len(res3) ==1:
        print(res3[0])
    else:
        print(sorted(res3)[1])

res4 = max(res)-min(res)
print(res4)











