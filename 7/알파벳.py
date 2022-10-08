# 백트래킹
import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([[0, 0, [board[0][0]]]])
maxlen = 1
while queue:
    k = queue.popleft()
    x = k[0]
    y = k[1]
    if len(k[2]) > maxlen:
        maxlen = len(k[2])
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in k[2]:
            lst = k[2] + [board[nx][ny]]
            queue.append([nx, ny, lst])
print(maxlen)