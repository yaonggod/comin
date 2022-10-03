import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, list(input().strip()))) for _ in range(n)]
# visited[x][y][0]은 벽 파괴 가능한 루트, visited[x][y][1]은 불가능한 루트
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0] = [1, 0]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, z):
    queue = deque([[x, y, z]])
    while queue:
        k = queue.popleft()
        x = k[0]
        y = k[1]
        z = k[2]
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                # 벽 부순 적 없는데 벽이 나타났다
                if matrix[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append([nx, ny, 1])
                # 갈 수 있음
                elif matrix[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append([nx, ny, z])
    return -1
                
print(bfs(0, 0, 0))








