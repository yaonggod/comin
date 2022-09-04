# https://www.acmicpc.net/problem/17836
from collections import deque
import sys
input = sys.stdin.readline 

n, m, t = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]
# 칼을 고려하지 않은 visited
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
# 칼을 고려한 visited
visited_sword = [[0] * m for _ in range(n)]
visited_sword[0][0] = 1
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 칼을 고려하지 않은 visited
queue = deque([[0, 0]])
while queue:
    k = queue.popleft()
    x = k[0]
    y = k[1]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and (miro[nx][ny] == 0 or miro[nx][ny] == 2) and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            queue.append([nx, ny])

go_without_sword = visited[n - 1][m - 1] - 1

# 검 찾기
sword_x = -1
sword_y = -1    
queue = deque([[0, 0]])
while queue:
    k = queue.popleft()
    x = k[0]
    y = k[1]
    if miro[x][y] == 2:
        # 검 위치
        sword_x = x
        sword_y = y
        # 검까지 가는 거리
        tosword = visited[x][y] - 1
        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and (miro[nx][ny] == 0 or miro[nx][ny] == 2) and visited_sword[nx][ny] == 0:
            visited_sword[nx][ny] = visited_sword[x][y] + 1
            queue.append([nx, ny])

# 검 못찾음 -> 검 없이 공주 찾기
if sword_x == sword_y == -1:
    # 공주에게 닿지 않음
    if go_without_sword == -1:
        print('Fail')
    else:
        # 공주에게 닿는 시간 초과
        if go_without_sword > t:
            print('Fail')
        # 성공
        else:
            print(go_without_sword)
            
# 검 찾음
else:      
    # 검 위치에서부터 bfs
    queue = deque([[sword_x, sword_y]]) 
    visited_sword = [[0] * m for _ in range(n)]
    visited_sword[sword_x][sword_y] = 1
    while queue:
        k = queue.popleft()
        x = k[0]
        y = k[1]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and (miro[nx][ny] == 0 or miro[nx][ny] == 1) and visited_sword[nx][ny] == 0:
                visited_sword[nx][ny] = visited_sword[x][y] + 1
                queue.append([nx, ny])  
                  
    go_with_sword = tosword + visited_sword[n - 1][m - 1] - 1
    # 검 없이 가기 실패
    if go_without_sword == -1:
        # 검 가지고 갔는데 시간 초과
        if go_with_sword > t:
            print('Fail')
        # 검 있이 성공
        else:
            print(go_with_sword)
    # 검 없이, 검 있이 둘 다 성공
    else:
        # 근데 둘 다 시간초과
        if min(go_without_sword, go_with_sword) > t:
            print('Fail')
        # 둘 중에 더 짧은 시간이 걸리는 걸로
        else:
            print(min(go_without_sword, go_with_sword))
    
    
    