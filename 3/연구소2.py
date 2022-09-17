from collections import deque
from itertools import combinations
from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
infected_lab = [[0] * n for _ in range(n)]

# 바이러스 위치 찾아서 조합 만들기에 사용
def findvirus(lab, n):
    lst = []
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 2:
                lst.append([i, j])
    return lst

# 감염된 부분을 1로 시작
def infection(lab, lst, n):
    for c in lst:
        lab[c[0]][c[1]] = 1
        
# 벽을 -1로 세움  
def wall(lab, new_lab, n):
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 1:
                new_lab[i][j] = -1

# 감염되지 않은 영역 찾기       
def findzero(lab, n):
    result = False
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 0:
                result = True
                break
    return result

# 감염되는데 걸리는 최대 시간 찾기  
def findmax(lab, n):
    max = 0
    for i in range(n):
        for j in range(n):
            if lab[i][j] > max:
                max = lab[i][j]
    return max
        
dx = [-1, 1, 0, 0]      
dy = [0, 0, -1, 1]
min_hour = 9999999

for comb in combinations(findvirus(lab, n), m):
    new_infected_lab = deepcopy(infected_lab)
    wall(lab, new_infected_lab, n)
    infection(new_infected_lab, comb, n)
    queue = deque(list(comb))
    while queue:
        c = queue.popleft()
        x = c[0]
        y = c[1]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and new_infected_lab[nx][ny] == 0:
                new_infected_lab[nx][ny] = new_infected_lab[x][y] + 1
                queue.append([nx, ny])
                
    # 1부터 시작했으므로 최대값에서 1을 빼주어야 함
    if not findzero(new_infected_lab, n) and min_hour > findmax(new_infected_lab, n) - 1:
        min_hour = findmax(new_infected_lab, n) - 1

# 모든 경우에서 모두 감염시키는데 실패했을 시
if min_hour == 9999999:
    print(-1)
else:   
    print(min_hour)


                    
        
