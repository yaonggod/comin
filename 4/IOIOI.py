import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()
p = 'I' + 'OI' * n

count = 0
for i in range(m - 2 * n):
    if s[i:i + 2 * n + 1] == p:
        count += 1
print(count)
        