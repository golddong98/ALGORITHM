# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
# 인풋값 빠르게 받기 위해
input = sys.stdin.readline

stack_in = []
stack_out = []

while True:
	user_input = input()
	# enq일 때
	if user_input[0:2] == 'en':
		# enq와 숫자 부분 나누기
		comd, num = user_input.split()
		# stack_in에 push
		stack_in.append(num)
	# deq일 때
	elif user_input[0:2] == 'de':
		# stack_out부분이 없을 때만 stack_in에 있는 숫자 채우기 작업 => 평균적으로 O(1)의 작업임
		if not stack_out:
			while stack_in:
				stack_out.append(stack_in.pop())
		# stack_out에서 가장 마지막에 있는 숫자 == Queue에서 가장 첫번째로 들어간 숫자
		if stack_out:
			val = stack_out.pop()
			print(val)
		# 없으면 EMPTY
		else:
			print('EMPTY')
	# exit일 때
	else:
		break

