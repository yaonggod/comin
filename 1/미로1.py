# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV14vXUqAGMCFAYD&categoryId=AV14vXUqAGMCFAYD&categoryType=CODE&problemTitle=%EB%AF%B8%EB%A1%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1

# 좌표 찾는 함수
def findxy(n, matrix):
    for i in range(16):
        for j in range(16):
            if matrix[i][j] == n:
                return [i, j]
                        
from collections import deque

for _ in range(1, 11):
    t = int(input())
    miro = [list(input()) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]
    start = findxy('2', miro)
    end = findxy('3', miro)
    queue = deque([start])
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 시작점에서부터 bfs해서 갈 수 있는 모든 곳들은 방문처리하기
    while queue:
        a = queue.popleft()
        x = a[0]
        y = a[1]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 16 and 0 <= ny < 16 and miro[nx][ny] != '1' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])          
    
    # 끝점이 방문처리가 되면 미로 탈출 성공, 아닐 시 실패
    if visited[end[0]][end[1]]:
        print('#{}'.format(t), 1)
    else:
        print('#{}'.format(t), 0)