# 출처: https://www.acmicpc.net/problem/2920

# tunes = list(map(int,input().split()))

# n = 6
# i = 0

# while i <= n:
#     if tunes[i]-tunes[i+1] == 1 or tunes[i]-tunes[i+1] == -1:

#         if i==6 and tunes[7] - tunes[6] == 1:
#             print('ascending')

#         if i==6 and tunes[7] - tunes[6] == -1:
#             print("descending")
#         i += 1
#     else:       
#         print('mixed')
#         break

    
note = [*map(int,input().split())]
if note == [1,2,3,4,5,6,7,8]:print('ascending')
elif note == [8,7,6,5,4,3,2,1]:print('desending')
else: print('mixed')










