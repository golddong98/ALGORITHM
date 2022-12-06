# 출처: https://www.acmicpc.net/problem/1157

a, b = map(int,input().split())

if a > b: print('>')
elif a < b: print('<')
else: print('==')