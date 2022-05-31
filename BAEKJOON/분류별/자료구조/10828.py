# 출처: https://www.acmicpc.net/problem/10828

#첫번째 풀이
from sys import stdin
a = int(stdin.readline())
stack = []

def func1(c):
    if c[:4] == 'push':
        num = c.split()[1]
        stack.append(num)
        return ''
    elif c[:3] == 'pop':
        return stack.pop() if stack else -1
    elif c[:4] == 'size':
        return len(stack)
    elif c[:5] == 'empty':
        return 0 if stack else 1
    elif c[:3] == 'top':
        return stack[-1] if stack else -1
    else:
        return 'hi'
result = ""

while a > 0:
    a = a-1
    result += (str(func1(stdin.readline())) + '\n')
print(result)

#함수에 넣어서 print하려고 하니까 값이 안나오는 append()의 경우
#None이 나와서 출력이 이상하게 됨
#None을 없애려고 ''로 해도 값으로 처리되서 출력이 이상하게됨


import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == 'push':
        value = word[1]
        stack.append(value)
    
    elif order == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
        
    elif order == 'size':
        print(len(stack))
    
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif order == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])

#바로 출력해서 해결