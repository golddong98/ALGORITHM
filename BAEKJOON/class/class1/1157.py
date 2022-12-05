# 출처: https://www.acmicpc.net/problem/1157

# dict={}

# l = list(input().upper())

# for i in l:
#     if dict.get(i): dict[i]+=1
#     else: dict[i]=1


# letter_list = sorted(dict.items(), key=lambda x: x[1], reverse=True)

# if letter_list[0][1] == letter_list[1][1] : print('?')
# else: print(letter_list[0][0])


import collections

l = list(input().upper())

most2=collections.Counter(l).most_common(2)



if len(most2) == 1: print(most2[0][0])
elif most2[0][1] == most2[1][1] : print('?')
else: print(most2[0][0])






