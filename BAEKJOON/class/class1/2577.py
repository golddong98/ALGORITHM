# 출처: https://www.acmicpc.net/problem/2577


# zero = [0 for _ in range(10)]

# mul = 1

# for _ in range(3):
#     mul *= int(input())

# mul_list = list(map(int, str(mul)))

# for i in mul_list:
#     zero[i] += 1

# for i in zero:
#     print(i)




a = int(input())
b = int(input())
c = int(input())

l = [*str(a*b*c)]

for number in range(10):
    print(l.count(str(number)))

