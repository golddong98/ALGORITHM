# 출처: https://www.acmicpc.net/problem/1546

# from functools import reduce

n = int(input())

scores = list(map(int, input().split()))

HIGHSCORE = max(scores)


# resultSum = reduce(lambda acc, cur: acc + cur/HIGHSCORE*100, scores, 0)

# print(resultSum/n)

result = 0

for i in scores:
    result += i/HIGHSCORE*100

print(result/n)























