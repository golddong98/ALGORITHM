# 출처:https://www.acmicpc.net/problem/1966

import sys,collections

input = sys.stdin.readline
queue = collections.deque

for _ in range(int(input().rstrip())):

    N, M = map(int, input().split())

    docs = queue(map(int, input().split()))
    docs_ = queue([0 for _ in range(N)])
    docs_[M] = 1
    cnt = 0
    while True:
        MAX = max(docs)
        check_docs = docs.popleft()
        check_docs_ = docs_.popleft()
        if check_docs == MAX:
            if check_docs_ != 1:
                cnt += 1
                
            else:
                cnt += 1
                print(cnt)
                break
        else:
            docs.append(check_docs)
            docs_.append(check_docs_)
                
    


# 순서 정해진거
# sorted()해서 뽑으면 됨

# 같은 수 중복된건
# 앞뒤생각 처음나온 같은 수 번호 + 앞뒤 수 + 1
# 1 2 1 3 1 4 1   같은 수 개수 

# 같은 수의 개수
 



