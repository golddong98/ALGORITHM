# 출처: https://www.acmicpc.net/problem/1920

# import sys

# N = sys.stdin.readline()
# A = list(sys.stdin.readline().rstrip().split(' '))
# M = int(sys.stdin.readline())
# MA = list(sys.stdin.readline().rstrip().split(' '))

# for el in MA:
#     for a in A:
#         if a == el:
#             print(1)
#             break
#     else:
#         print(0)
    
#         # if a == el:
#         #     print(1)
#         #     break
#         # else:
#         #     print(0)
        

# import sys

# N = sys.stdin.readline()
# A = sorted(list(map(int,sys.stdin.readline().rstrip().split(' '))))
# M = int(sys.stdin.readline())
# MA = list(map(int,sys.stdin.readline().rstrip().split(' ')))

# if len(A)%2 ==0:
#     mid = int(len(A)/2)
# else:
#     mid = int((len(A)-1)/2)


# for el in MA:
#     if el <= A[mid]:
#         for i in range(mid+1):
#             if el == A[i]:
#                 print(1)
#                 break
#         else:
#             print(0)
#     else:
#         for i in range(len(A)-1,mid,-1):
#             if el == A[i]:
#                 print(1)
#                 break
#         else:
#             print(0)
        
# input_num = int(input())
# numbers = list(map(int, input().split()))
# numbers.sort()

# input_num2 = int(input())
# numbers2 = list(map(int, input().split()))
    
        
# for num in numbers2:
#     left, right = 0, len(numbers) -1

#     is_find = False

#     while True:
#         median = (left + right) //2
#         if num == numbers[median]:
#             print(1)
#             is_find = True
#             break
#         elif num > numbers[median]:
#             left = median + 1
#         elif num < numbers[median]:
#             right = median - 1

#         if left > right:
#             break
    
#     if not is_find:
#         print(0)


    
from sys import stdin

n = stdin.readline()
N = sorted(map(int, stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())

# l: target 숫자
# N: target과 비교할 숫자들
# start: N의 시작 번째
# end: N의 끝 번째

def binary(l, N, start, end):
    if start> end:
        return 0
    m = (start+ end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l,N,start, end))

# start와 end에 1을 더해주고 빼주는 이유:
# 첫번째 (start+end)//2 를 m이라하고
# 두번째 (start+end)//2 를 m2라하면
# 반복을 없애기 위해서는 m != m2이여야 한다.
# m == m2이면 계속 값이 반복되서 재귀문을 빠져나오질 못한다.

# 그럼 1이란 숫자는 어떻게 나온걸까?

# 증명:

# a, b = start, end라 하자 => a<=m<b
# 1) (a + b)가 짝수이고
#target숫자가 작았을 때 즉, 위의 식에서는 l < N[m]일때


#  a+b <= m+b (a<=m 이므로)
# 1 안 더했을 때
# m = (a+b)//2 = (a+b)/2 <= (m+b)//2 =(m+1+b)//2 (m은 홀수이므로)= m+b/2 = m2(같을 수 있음)
# 1더했을때
# (a+b)//2 = (a+b)/2 < (m+b+1)//2 = (m+1+b+1)//2 (m은 홀수이므로)= m+b/2+1 =m2(같을 수 없음)

#target숫자가 클 때 즉, 위의 식에서는 l > N[m]일때

# a+m < a+b (m<b이므로)
# 1 안 뺐을 때
# m = (a+b)//2 = (a+b)/2 > (a + m)//2 = (a+m-1)//2 = (a+m-1)/2=m2 (같을 수 없음) 

# 1 뺏을 때
# 위 식으로 부터 같을 수 없다는 바로 알 수 있음

# 2) (a + b)가 홀수일 때


# (a+b)가 짝 수일 때와 같은 과정을 적용하면 m과 m2가 같지 않기 위해서는  1>N[m]일 때 1을 빼야 됨을 알 수 있음
# 따라서 1을 m에 더하고 빼줘야 m2가 m과 다른 값인 m2가 되어서 반복을 하는 걸 알 수 있음




