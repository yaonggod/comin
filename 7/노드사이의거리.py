# dfs
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = 1000000000
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(n + 1):
    graph[_][_] = 0
for _ in range(n - 1):
    i, j, length = map(int, input().split())
    graph[i][j] = length
    graph[j][i] = length
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
for _ in range(m):
    a, b = map(int, input().split())
    print(graph[a][b])