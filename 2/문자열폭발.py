# https://www.acmicpc.net/problem/9935
import sys
input = sys.stdin.readline
word = list(input().strip())
explode = list(input().strip())
n = len(explode)

# replace로 쓰면 시간초과
stack = []
for letter in word:
    stack.append(letter)
    if stack[-n:] == explode:
        for _ in range(n):
            stack.pop()
                        
if stack == []:
    print('FRULA')
else:
    print(*stack, sep='')
    
