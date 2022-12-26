# 출처: https://www.acmicpc.net/problem/1654

import sys

input = sys.stdin.readline

K, N = map(int, input().split())

lines = []

for _ in range(K):
    lines.append(int(input())) 

start = 1
end = max(lines)

while start <=end :
    mid = (start+end)//2
    cnt = 0

    for i in range(K):
        cnt += lines[i]//mid
    
    if cnt < N:
        end = mid -1
    
    else:
        start = mid +1

print(end)

# 이분탐색 
# BigO: O(log N)
# 정렬된 자룔르 반으로 나누어 탐색하는 방법
# 주의점: 자료는 오름차순으로 정렬된 자료여야 함
# 이진트리, 바이너리서치는 코딩 인터뷰 단골문제

# share = MAX // N

# while True:
#     result = reduce(lambda acc, cur: acc+cur//share  ,lines,0)
#     if result == N:
#         break
#     # 
#     mul = result // N
#     if mul >1:
#         share *= mul
#     else:
#         share += 1
#     # 

# while True:
#     result = reduce(lambda acc,cur: acc+cur//share, lines, 0)
#     if result != N:
#         break
#     share += 1

# print(share -1)
        









