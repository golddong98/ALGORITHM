# 출처: https://www.acmicpc.net/problem/1978

# _ = input()
# prob = list(map(int,input().split()))

# MAX = max(prob)
# nums = [i for i in range(2, MAX+1)]
# primes = []

# while nums:
#     prime = nums[0]
#     primes.append(prime)
#     for k in nums:
#         if k % prime ==0:
#             nums.remove(k)

# cnt = 0
# for i in prob:
#     if i in primes:
#         cnt += 1

# print(cnt)
        

n = input()
nums = list(map(int, input().split()))

resCnt = 0

for i in nums:
    cnt = 0
    if i ==1:
        continue
    for j in range(2,i+1):
        if i % j == 0:
            cnt +=1
    if cnt ==1:
        resCnt +=1
print(resCnt)
            

