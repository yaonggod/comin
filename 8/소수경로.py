import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

prime = [True] * 10000
prime[0] = False
prime[1] = False
for i in range(2, 10000):
    if prime[i] == True:
        j = 2
        while i * j < 10000:
            prime[i * j] = False
            j += 1
                    
def bfs(a):
    global result
    queue = deque()
    queue.append(a)
    while queue:
        k = queue.popleft()
        if k == b:
            result = visited[int(''.join(k))]
            break
        for i in range(4):
            for j in range(10):
                n_k = deepcopy(k)
                n_k[i] = str(j)
                if 1000 <= int(''.join(n_k)) < 10000 and prime[int(''.join(n_k))] and visited[int(''.join(n_k))] == -1:
                    visited[int(''.join(n_k))] = visited[int(''.join(k))] + 1
                    queue.append(n_k)            
            
t = int(input())
for _ in range(t):
    result = 'impossible'
    a, b = map(str, input().split())
    a = list(a)
    b = list(b)
    visited = [-1] * 10000
    visited[int(''.join(a))] = 0
    bfs(a)
    print(result)
    
    