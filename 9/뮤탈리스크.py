import sys
input = sys.stdin.readline
from itertools import permutations
from collections import deque

n = int(input())
scv = list(map(int, input().split()))

# 9로만 때리기
if n == 1:
    print(scv[0] // 9 + 1)

# 9, 3으로만 때리기
elif n == 2:
    start = [scv + [0]]
    visited = [[False] * 61 for _ in range(61)]
    queue = deque(start)
    while queue:
        a = queue.popleft()
        if a[0] == 0 and a[1] == 0:
            print(a[2])
            break
        else:
            if not visited[max(a[0] - 9, 0)][max(a[1] - 3, 0)]:
                new1 = [max(a[0] - 9, 0), max(a[1] - 3, 0), a[2] + 1] 
                queue.append(new1)
            if not visited[max(a[0] - 3, 0)][max(a[1] - 9, 0)]:
                new1 = [max(a[0] - 3, 0), max(a[1] - 9, 0), a[2] + 1] 
                queue.append(new1)
            
# 9, 3, 1로 때리기
elif n == 3:
    start = [scv + [0]]
    visited = [[[False] * 61 for _ in range(61)] for _ in range(61)]
    queue = deque(start)
    while queue:
        a = queue.popleft()
        if a[0] == 0 and a[1] == 0 and a[2] == 0:
            print(a[3])
            break
        else:
            for c in permutations([9, 3, 1], 3):
                if not visited[max(a[0] - c[0], 0)][max(a[1] - c[1], 0)][max(a[2] - c[2], 0)]:
                    new = [max(a[0] - c[0], 0), max(a[1] - c[1], 0), max(a[2] - c[2], 0), a[3] + 1]
                    queue.append(new)
                

                
        
        
    
    
    

