import sys
# input 시간을 좀 더 줄여주기 위해서
input = sys.stdin.readline


# 최대값을 뽑기위한 스택
max_stack = []
# 출력하기 위한 스택
stack = []
while True:
	user_input = input()
	if user_input[0:2] == 'pu':
		# push일 때 명령과 숫자를 나눔
		comd, num = user_input.split()
		# 스택에 추가
		num = int(num)
		stack.append(num)
		# 최대값 스택에도 추가 후 max연산을 O(1)로 하기 위해 미리 sort해줌
		if not max_stack or max_stack[-1] <= num:
			max_stack.append(num)
	elif user_input[0:2] == 'po':
		# pop하기 전에 stack있는지 확인
		if stack:
			# 스택에서 제외
			val = stack.pop()
			# val와 최대값 스택에서 뽑은 최대값과 같으면 제외
			if val == max_stack[-1]:
				max_stack.pop()
			print(val)
		else:
			print('EMPTY')
	elif user_input[0:2] == 'ma':
		# stack이 있는지 확인
		if max_stack:
			print(max_stack[-1])
		else:
			print('EMPTY')
	else:
		break