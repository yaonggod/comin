import sys
sys.stdin = open("4\봄버맨.txt")
r, c, n = map(int, input().split())
land = [list(input().strip()) for _ in range(r)]
for i in range(r):
    for j in range(c):
        if land[i][j] == '.':
            land[i][j] = -1
        else:
            land[i][j] = 0
            
def second(r, c, land):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    lst = []
    for i in range(r):
        for j in range(c):
            land[i][j] += 1
            if land[i][j] == 3:
                land[i][j] = 0
                lst.append([i, j])
    for l in lst:
        x = l[0]
        y = l[1]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c:
                land[nx][ny] = 0
                
def setbomb(r, c, land):
    for i in range(r):
        for j in range(c):
            if land[i][j] == 0:
                land[i][j] = 1
                        

for i in range(n - 1):
    second(r, c, land)
  
from pprint import pprint
pprint(land)  
            
