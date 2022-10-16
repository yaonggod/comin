import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
visited = set()
start = list(map(int, input().split()))
end = list(map(int, input().split()))
# 동 서 남 북
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]
def change_dir(dir, target):
    if (dir, target) in [(1, 2), (2, 1), (3, 4), (4, 3)]:
        change = 2
    elif dir == target:
        change = 0
    else:
        change = 1
    return change

queue = deque([[start[0] - 1, start[1] - 1, start[2], 0]])
result = []
while queue:
    x, y, d, cnt = queue.popleft()
    print('--------')
    print(x, y, d, cnt)
    print()
    if x == end[0] - 1 and y == end[1] - 1:
        result.append(cnt + change_dir(dir, end[2]))
    for i in range(1, 4):
        nx = x + dx[d] * i
        ny = y + dy[d] * i
        if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] == 0:
            if (nx, ny, d, cnt + 1) not in visited:
                queue.append((nx, ny, d, cnt + 1))
                visited.add((nx, ny, d, cnt + 1))
                print(nx, ny, d, cnt + 1)
        else:
            break
    for i in range(1, 5):
        if i != d and (x, y, i, cnt + 1) not in visited:
            queue.append((x, y, i, cnt + change_dir(d, i)))
            visited.add((x, y, i, cnt + change_dir(d, i)))
            print(x, y, i, cnt + change_dir(d, i))
            
print(result)
        

