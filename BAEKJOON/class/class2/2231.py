# 출처:https://www.acmicpc.net/problem/2231

n = int(input())

i=1

flag = True
while flag:
    a = map(int,list(str(i)))
    result = i + sum(a)
    if n == result:
        print(i)
        flag = False
    i += 1
    if n <= i:
        break
if flag:    
    print(0)

# for i in range(n):
#     a = map(int,list(str(i)))
#     result = i + sum(a)
#     if n == result:
#         print(i)
#         break

