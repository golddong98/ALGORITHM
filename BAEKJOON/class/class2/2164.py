# 출처:https://www.acmicpc.net/problem/2164

import collections

deq = collections.deque


N = int(input())

cards = deq([i for i in range(N)])

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0]+1)