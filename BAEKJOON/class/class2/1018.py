# 출처: https://www.acmicpc.net/problem/1018

import sys
# 입력값많으니까 sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = []
result = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0
    
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 ==0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
        result.append(draw1)
        result.append(draw2)

print(min(result))


    





# 0이 아닌 이상 다 봐야됨

