# 출처: https://www.acmicpc.net/problem/2908

# a, b = map(reversed, input().split())

# a_num=''
# b_num=''

# for n in a:
#     a_num += n

# for n in b:
#     b_num += n

# print(max(int(a_num),int(b_num))) 


# print(max(list(map(int,input()[::-1].split()))))



n = input()[::-1]

print(n)