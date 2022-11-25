import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
lst = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            lst.append(i)
            lst.append(j)
lst.append(0)
queue = deque(lst)
while queue:
    x1, y1, x2, y2, t = queue.popleft()
    if x1 == x2 and y1 == y2:
        pass
    elif not(0 <= x1 < n and 0 <= y1 < m) and (0 <= x2 < n and 0 <= y2 < m):
        print(t)
        break
    elif (0 <= x1 < n and 0 <= y1 < m) and not (0 <= x2 < n and 0 <= y2 < m):
        print(t)
        break
    else:
        for d in range(4):
            nx1 = x1 + dx[d]
            ny1 = y1 + dy[d]
            nx2 = x2 + dx[d]
            ny2 = y2 + dy[d]
            
