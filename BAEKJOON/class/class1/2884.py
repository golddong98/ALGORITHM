# 출처: https://www.acmicpc.net/problem/2884

# h, m = map(int,input().split())

# if m>=45:
#     print(f"{h} {m-45}")
# else:
#     if not h == 0:
#         print(f"{h-1} {m+15}")
#     else:
#         print(f"{23} {m+15}")


a,b=map(int,input().split())
print((a-(b<45))%24,(b-45)%60)


# m-=45
# if m<0:
#     m+=60
#     n-=1
#     if n<0:
#         n+=24
# print(n,m)