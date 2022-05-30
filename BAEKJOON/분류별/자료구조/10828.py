# 출처: https://www.acmicpc.net/problem/10828
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

while a > 0:
    a = a-1
    print(str(func1(stdin.readline())))
