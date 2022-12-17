# 출처: https://www.acmicpc.net/problem/10871

n, x = map(int,input().split())

seq = list(map(int, input().split()))

res = []

for i in seq:
    if x >i:
        res.append(i)

print(*res)



