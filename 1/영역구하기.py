# https://www.acmicpc.net/problem/2583

from collections import deque

# 행 : m, 열 : n -> x는 n에, y는 m에
m, n, k = map(int, input().split())
paper = [[0] * n for _ in range(m)]
# 영역 채우기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[j][i] = 1
            
# 빈 공간에 해당하는 부분을 넣기                   
blank = []
visited = [[False] * n for _ in range(m)]        
for i in range(m):
    for j in range(n):
        # 빈 공간이 시작하는 점
        if paper[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            queue = deque([[i, j]])
            area = 1
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            # bfs를 끝내면 빈 공간 하나가 완성됨
            while queue:
                a = queue.popleft()
                x = a[0]
                y = a[1]
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < m and 0 <= ny < n and paper[nx][ny] == 0 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append([nx, ny])
                        area += 1
            # 완성된 빈 공간을 blank에 넣어줌
            blank.append(area)

blank.sort() 
print(len(blank))
print(*blank)  