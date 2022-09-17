import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)    
visited = [False] * (n + 1)
for g in graph:
    g.sort()

visited[r] = True
lst = [r]

def dfs(v):
    for e in graph[v]:
        if not visited[e]:
            lst.append(e)
            visited[e] = True
            dfs(e)

dfs(r)  

for i in range(1, n + 1):
    try:
        print(lst.index(i) + 1)
    except:
        print(0)
        
