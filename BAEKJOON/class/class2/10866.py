# 출처:https://www.acmicpc.net/problem/10866


import collections, sys

deq = collections.deque
input = sys.stdin.readline

result_list = deq()

for _ in range(int(input())):
    comd_sentence = input().rstrip()
    if comd_sentence[0] =='p' and comd_sentence[1] =='u':
        comd, num = comd_sentence.split()
        if comd == 'push_back':
            result_list.append(num)
        else:
            result_list.appendleft(num)
    elif comd_sentence == 'pop_front':
        if not result_list:
            print(-1)
        else:
            result = result_list.popleft()
            print(result)
    elif comd_sentence == 'pop_back':
        if not result_list:
            print(-1)
        else:
            result = result_list.pop()
            print(result)
    elif comd_sentence == 'size':
        print(len(result_list))
    elif comd_sentence == 'empty':
        if not result_list:
            print(1)
        else:
            print(0)
    elif comd_sentence == 'front':
        if not result_list:
            print(-1)
        else:
            print(result_list[0])
    else:
        if not result_list:
            print(-1)
        else:
            print(result_list[-1])