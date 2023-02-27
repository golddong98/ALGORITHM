# 출처:https://www.acmicpc.net/problem/2805

# N, M = map(int, input().split())

# trees = sorted(map(int, input().split()), reverse=True)

# start = 0
# end = len(trees)-1

# cut_tree = trees[(start+end)//2]

# get_tree = 0
# while get_tree < M:
#     get_tree = 0
#     for tree in trees:
#         if tree > cut_tree:
#             get = tree - cut_tree
#             get_tree += get
#         else:
#             break
    

# print(cut_tree+1)


# # max_tree

# # print(round(4/2));

def binary_search(arr, val, low, high):
    if low > high:
        return False #해당 배열에 타겟 숫자 미존재

    mid = (low + high) //2 #위치 기반으로 찾는 것

    if arr[mid] > val:
        return binary_search(arr, val, low, mid-1) #수가 중앙값보다 아래있는 경우
    elif arr[mid] < val:
        return binary_search(arr, val, mid+1, high) #수가 중앙 값보다 위에 있는 경우
    else:
        return True #아니면 숫자를 출려 -> return val

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) //2

    log = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid
    
    if log >= M:
        start = mid +1
    else:
        end = mid -1
print(end)