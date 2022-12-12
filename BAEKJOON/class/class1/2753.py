# 출처: https://www.acmicpc.net/problem/2753

# year = int(input())

# if not year%4 ==0:
#     print('0')
# else:
#     if not year % 100 == 0 or year%400 == 0:
#         print('1')
#     else:
#         print('0')


year=int(input())
if year%4==0 and (year%100!=0 or year%400==0):
    print(1)
else:
    print(0)