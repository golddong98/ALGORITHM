# 출처: https://www.acmicpc.net/problem/2475

# from sys import stdin


# li = []

# for _ in range(9):
#     li.append(int(stdin.readline()))

# max = max(li)

# print(max)
# print(li.index(max)+1)




n = [int(input()) for _ in range(9)]

k = max(n)

print(k)
print(n.index(k)+1)







