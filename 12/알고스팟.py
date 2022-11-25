import sys
input = sys.stdin.readline
from collections import deque
m, n = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
visited[0][0] = 0
queue = deque([[0, 0]])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
c = 1
while queue:
    if visited[n - 1][m - 1][0] != -1:
        print(c)
        break
        
