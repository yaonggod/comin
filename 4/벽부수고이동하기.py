import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
visited = [[[-1, 0] for _ in range(m)] for _ in range(n)]
visited[0][0] = [1, 0]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([[0, 0]])
while queue:
    k = queue.popleft()
    x = k[0]
    y = k[1]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        # 영역 내에 있고 안 간 곳이다
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][0] == -1:
            # 벽을 부순 전적이 없다
            if visited[x][y][1] == 0:
                # 앞에 벽이 없다
                if matrix[nx][ny] == '0':
                    visited[nx][ny] = [visited[x][y][0] + 1, 0]
                    queue.append([nx, ny])
                # 앞에 벽이 있다 -> 부순다
                else:
                    visited[nx][ny] = [visited[x][y][0] + 1, 1]
                    queue.append([nx, ny])
            # 벽을 부순 전적이 있다
            elif visited[x][y][1] == 1:
                # 앞에 벽이 없다
                if matrix[nx][ny] == '0':
                    visited[nx][ny] = [visited[x][y][0] + 1, 1]
                    queue.append([nx, ny])
                # 앞에 벽이 있으면 못감

print(visited[n - 1][m - 1][0])






