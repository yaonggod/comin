# https://www.acmicpc.net/problem/16120
import sys
input = sys.stdin.readline
word = list(input().strip())

# replace로 쓰면 시간초과
stack = []
for letter in word:
    stack.append(letter)
    try:
        if stack[-4:] == ['P', 'P', 'A', 'P']:
            for _ in range(3):
                stack.pop()
    except:
        pass

if stack == ['P']:
    print('PPAP')
else:
    print('NP')      

