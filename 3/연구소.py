import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 벽을 세우는 조합을 짤 때와 감염되지 않은 영역의 너비 구할 떄 활용
def find_zero(lab, n, m):
    lst = []
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lst.append([i, j])
    return lst

# 벽 세우기
def make_new_walls(lst, new_lab):
    for x in lst:
        new_lab[x[0]][x[1]] = 1

# 벽 조합    
walls_comb = list(combinations(find_zero(lab, n, m), 3))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_safe_zone = 0
for c in walls_comb:
    # 딥카피를 해야 원본 lab이 변하질 않음
    new_lab = deepcopy(lab)
    make_new_walls(c, new_lab)
    # 감영시키기
    for i in range(n):
        for j in range(m):
            if new_lab[i][j] == 2:
                queue = deque([[i, j]])
                while queue:
                    k = queue.popleft()
                    x = k[0]
                    y = k[1]
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m and new_lab[nx][ny] == 0:
                            new_lab[nx][ny] = 2
                            queue.append([nx, ny])
    safe_zone = len(find_zero(new_lab, n, m))
    if safe_zone > max_safe_zone:
        max_safe_zone = safe_zone

print(max_safe_zone)           

                
    


    
