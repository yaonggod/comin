# 둥지 s, 치즈공장 숫자, 방해물 x, 빈 공간 .
# 쥐는 둥지에서 나와서 모든 치즈 공장을 방문해 치즈를 한개씩 먹음
# 치즈공장 n개, 치즈 한 종류씩 생산, 경도는 다 다름, 1부터 n까지의 경도의 치즈를 생산하는 공장이 하나씩 있음
# 체력 1로 시작해서 치즈 먹으면 체력이 1씩 증가하는데 자신의 체력보다 딱딱한 치즈를 먹는 것은 불가
# 즉 1부터 9까지 차례대로 먹어야함
# 쥐는 1분에 동서남북 한 칸 이동, 방해물은 못가, 치즈 먹는 시간은 무시
# 치즈 공장을 치즈를 안먹고 지나가는 것도 가능
# 모든 치즈를 먹기까지 걸리는 최단시간 측정, 모든 치즈를 다 먹을 수 있다고 보장

# h 높이 w 너비 n 경도

import sys
from collections import deque
input = sys.stdin.readline

h, w, n = map(int, input().split())
cheese = [list(input().strip()) for _ in range(h)]

def findposition(h, w, x : str):
    for i in range(h):
        for j in range(w):
            if cheese[i][j] == x:
                return [i, j]
            
start_x = findposition(h, w, 'S')[0]
start_y = findposition(h, w, 'S')[1]

moves = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 둥지에서 1번까지
visited = [[-1] * w for _ in range(h)]
visited[start_x][start_y] = 0
queue = deque([[start_x, start_y]])
while True:
    k = queue.popleft()
    x = k[0]
    y = k[1]
    if k == findposition(h, w, '1'):
        moves += visited[x][y]
        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < h and 0 <= ny < w and cheese[nx][ny] != 'X' and visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            queue.append([nx, ny])

# 번호 간 이동
for i in range(1, n):
    visited = [[-1] * w for _ in range(h)]
    i_x = findposition(h, w, str(i))[0]
    i_y = findposition(h, w, str(i))[1]
    visited[i_x][i_y] = 0
    queue = deque([[i_x, i_y]])
    while True:
        k = queue.popleft()
        x = k[0]
        y = k[1]
        if k == findposition(h, w, str(i + 1)):
            moves += visited[x][y]
            break
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < h and 0 <= ny < w and cheese[nx][ny] != 'X' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
                
print(moves)
    
    
    
 



            

            


