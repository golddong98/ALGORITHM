# 출처:https://www.acmicpc.net/problem/11050

import sys
input = sys.stdin.readline

N,K = map(int,input().split())

# result = 1
# for i in range(K):
#     result *= N
#     N -= 1

# divisor =1
# for i in range(2, K+1):
#     divisor *= i
# print(result // divisor)

def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(N) // (factorial(N-K) * factorial(K)))