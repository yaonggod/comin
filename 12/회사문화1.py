import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst2 = []
for _ in range(m):
    lst2.append(list(map(int, input().split())))
    
