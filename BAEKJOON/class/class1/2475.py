# 출처: https://www.acmicpc.net/problem/2475

nums = list(map(int,input().split()))

result = 0

for n in nums:
    result += n**2

print(result%10)





# print(10%3)