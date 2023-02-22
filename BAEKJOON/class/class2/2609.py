# 출처:https://www.acmicpc.net/problem/2609

n,m = map(int,input().split(' '))

mini = min(n,m)

while True:
    if n%mini ==0 and m %mini ==0:
        print(mini)
        break
    mini -= 1

a =1
b =1
while True:
    if n*a > m*b:
        b +=1
    elif n*a < m*b:
        a +=1
    else:
        print(n*a)
        break