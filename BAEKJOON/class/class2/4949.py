# 출처:https://www.acmicpc.net/problem/4949

import sys
input = sys.stdin.readline
while True:
    str_val = input()
    괄호 = []
    result = True
    if str_val == '.':
        break
    for word in str_val:
        if word == '(' or word == '[':
            괄호.append(word)
        elif word == ')':
            if len(괄호) !=0 and 괄호[-1] == '(':
                괄호.pop()
            else:
                result = False
                break
        elif word == ']':
            if len(괄호) !=0 and 괄호[-1] == '[':
                괄호.pop()
            else:
                result = False
                break
    if not 괄호 and result ==True:
        print("yes")
    else:
        print('no')

