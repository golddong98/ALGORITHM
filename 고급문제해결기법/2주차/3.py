def solve(A):
	# return a list B such that B[0] <= B[1] >= B[2] <= B[3] ...
	# 파이썬에서 Timsort 알고리즘을 쓰는 sort함수의 시간복잡도: O(n log n)
	A.sort()
	# 홀수 자리, 짝수 자리에 있는 원소를 바꾸는 알고리즘은 (n-1)/2 번 반복함. 여기서 시간 복잡도는 상수를 고려하지 않고 n에 대한 복잡도만을 분석하기 때문에 O(n)이라고 표현가능.
	for i in range(1, len(A)-1):
		if i != (len(A)-1) and i%2 == 1:
			A[i], A[i+1] = A[i+1], A[i]
	# 따라서 전체 시간복잡도는 O(n log n) + O(n)이 됨. 일반적으로 복잡도를 분석할 때 가장 높은 차수의 항을 우선적으로 고려하기 때문에 여기서는 O(n lon n)이 가장 높은 차수의 항이므로 결론적으로 시간복잡도는 O(n log n)이 됨.
	return A
