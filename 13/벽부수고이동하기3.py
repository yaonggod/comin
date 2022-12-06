import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

queue = deque()
queue.append((0, 0, 0, 1, True))
result = -1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while queue:
    x, y, z, b, a = queue.popleft()
    if x == n - 1 and y == m - 1:
        result = b
        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            # 뿌순다
            if board[nx][ny] == 1 and z < k and a and visited[nx][ny][z + 1] == 0:
                visited[nx][ny][z + 1] = visited[x][y][z] + 1
                queue.append((nx, ny, z + 1, b + 1, False))
            # 안뿌순다
            elif board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                if a:
                    queue.append((nx, ny, z, b + 1, False))
                else:  
                    queue.append((nx, ny, z, b + 1, True))
    # 가만히 있는건 밤에만 하는걸로
    if not a:
        queue.append((x, y, z, b + 1, True))
    # print(queue)

print(result)          
