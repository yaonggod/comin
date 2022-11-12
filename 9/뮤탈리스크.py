import sys
input = sys.stdin.readline
from itertools import permutations
from collections import deque

n = int(input())
scv = list(map(int, input().split()))

if len(scv) == 1:
    start = scv + [0, 0, 0]
elif len(scv) == 2:
    start = scv + [0, 0]
else:
    start = scv + [0]
visited = [[[False] * 61 for _ in range(61)] for _ in range(61)]
queue = deque([start])
while queue:
    a = queue.popleft()
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        print(a[3])
        break
    else:
        for c in permutations([9, 3, 1], 3):
            if not visited[max(a[0] - c[0], 0)][max(a[1] - c[1], 0)][max(a[2] - c[2], 0)]:
                visited[max(a[0] - c[0], 0)][max(a[1] - c[1], 0)][max(a[2] - c[2], 0)] = True
                new = [max(a[0] - c[0], 0), max(a[1] - c[1], 0), max(a[2] - c[2], 0), a[3] + 1]
                queue.append(new)
                

# from pprint import pprint
# visited = [[[False] * 3 for _ in range(3)] for _ in range(3)]
# pprint(visited)

# print(list(permutations([9, 3, 1], 3)))
    
