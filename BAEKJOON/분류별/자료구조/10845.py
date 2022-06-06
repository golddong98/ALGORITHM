import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()

for _ in range(N):
    command = sys.stdin.readline().rstrip().split(' ')
    text = command[0]
    if text == 'push':
        number = command[1]
        queue.append(number)
    elif text == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif text == 'size':
        print(len(queue))
    elif text == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif text == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    else:
        if not queue:
            print(-1)
        else:
            print(queue[-1])

#deque 모듈 가져와서 큐구현

import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()

for _ in range(N):
    command = sys.stdin.readline().rstrip().split(' ')
    text = command[0]
    if text == 'push':
        number = command[1]
        queue.append(number)
    elif text == 'pop':
        if not queue : print(-1)
        else: print(queue.popleft())
    elif text == 'size':
        print(len(queue))
    elif text == 'empty':
        if not queue : print(1)
        else: print(0)
    elif text == 'front':
        if not queue : print(-1)
        else: print(queue[0])
    else:
        if not queue : print(-1)
        else: print(queue[-1])

#두번째는 if else문 더 짧게 해서 코드 줄 줄여봄