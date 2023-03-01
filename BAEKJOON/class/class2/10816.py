# 출처:https://www.acmicpc.net/problem/10816

import sys
input = sys.stdin.readline

N = int(input())

cards = list(map(int,input().split()))

M = int(input())

question_numbers = list(map(int,input().split()))


# # 이분 탐색

# cards = sorted(cards)

# cnts = []

# for q_n in question_numbers:
#     start = 1
#     end = len(cards)
#     cnt = 0
#     while start <= end:
#         mid = (start+end)//2
#         if cards[mid] < q_n:
#             start = mid+1
#         elif cards[mid] > q_n:
#             end = mid-1
#         else:
#             cnt +=1
#             left, right = mid-1, mid+1
#             len_cards = len(cards)
#             while left != -1 and (q_n == cards[left]):
#                 cnt += 1
#                 left -=1
#             while right !=len_cards and (q_n == cards[right]):
#                 cnt +=1
#                 right +=1
#             break
#     cnts.append(cnt)

# print(*cnts)

# => 시간초과 왼쪽오른쪽으로 가는 부분에서 시간 많이 잡아먹는듯

# count

from collections import Counter

c = Counter(cards)

cnts=[]

for q_n in question_numbers:
    cnts.append(c[q_n])

print(*cnts)


