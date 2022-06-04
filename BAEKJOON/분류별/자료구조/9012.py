# 출처: https://www.acmicpc.net/problem/9012

import sys

N = int(sys.stdin.readline())


for _ in range(N):
    stack = []
    vps = list(sys.stdin.readline().rstrip())
    for i in range(len(vps)):
        if vps[i] == '(':
            stack.append(vps[i])
        elif not stack and vps[i] == ')':
            stack.append('hi')
            break
        else:
            stack.pop()  
    if not stack:
        print('YES')
    else:
        print('NO')
    
# break로 빠져 나온 stack과 break를 거치지 않은 stack을 구분해야 되는데
# 못하겠어서 그냥 stack에 아무거나 집어넣어서 차이를 만들어줌

import sys

N = int(sys.stdin.readline())


for _ in range(N):
    stack = []
    vps = list(sys.stdin.readline().rstrip())
    for i in range(len(vps)):
        if vps[i] == '(':
            stack.append(vps[i])
        elif not stack and vps[i] == ')':
            print('NO')
            break
        else:
            stack.pop()  
    else:
        if not stack:
            print('YES')
        else:
            print('NO')
    
    
# break를 거치지 않은 것은 쌩 else 쓰면 됨