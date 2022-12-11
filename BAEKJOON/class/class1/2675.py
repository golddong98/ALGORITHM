# 출처: https://www.acmicpc.net/problem/2675

test_num = int(input())

for _ in range(test_num):
    r, s = input().split()
    result = ''
    r = int(r)
    for i in s:
        result += i*r
    print(result)
        
