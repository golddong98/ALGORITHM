# 출처:https://www.acmicpc.net/problem/1463

N = int(input())

d = [0]*(N+1)

for i in range(2, N+1):
    d[i]=d[i-1]+1 #1을 빼줌 ->1회 진행 그 전꺼랑 적어도 1차이난다.
    if i%2==0: #2로 나누어 떨어질 때 2로 나누어줌
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0: #3으로 나누어 떨어질 때 3으로 나누어줌
        d[i]=min(d[i],d[i//3]+1)
print(d[N])