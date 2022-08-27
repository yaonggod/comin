# https://www.acmicpc.net/problem/1697

from collections import deque
n, k = map(int, input().split())

queue = deque([n])
visited = [0] * 100001
while True:
    x = queue.popleft()
    if x == k:
        break
    # 한 단계씩 더해나감
    # 앞으로 이동
    if 0 <= x + 1 <= 100000 and visited[x + 1] == 0:
        visited[x + 1] = visited[x] + 1
        queue.append(x + 1)
    # 뒤로 이동
    if 0 <= x - 1 <= 100000 and visited[x - 1] == 0:
        visited[x - 1] = visited[x] + 1
        queue.append(x - 1)
    # 순간이동
    if 0 <= x * 2 <= 100000 and visited[x * 2] == 0:
        visited[x * 2] = visited[x] + 1
        queue.append(x * 2)
            
print(visited[k])