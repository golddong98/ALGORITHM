# 출처:https://www.acmicpc.net/problem/2292

n = int(input())

# if n ==1:
#     print(1)
# else:
#     i = 1
#     while True:
#         if 1 + 6*(i*(i+1)/2-i) < n:
#             i += 1
#         else:
#             print(i)
#             break
    
beeHouse = 1
c = 1

while n > beeHouse:
    beeHouse += 6*c
    c += 1

print(c)


# 1 + 

# 1+6(k(k+1)/2-k)
# k = 1 -> 1
# k = 2 -> 7
# k = 3 -> 19
# k = 4 -> 37

# 1 2 8 20
# 1 + 1
# 1 + 1 + 6



# 1    1
# 2~7  6   
# 8~19 12
# 20~37 18
#        24
#        ...