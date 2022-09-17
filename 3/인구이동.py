import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def people_move(lst):
    m = len(lst)
    people_sum = 0
    for c in lst:
        people_sum += people[c[0]][c[1]]
    result = people_sum // m
    for c in lst:
        people[c[0]][c[1]] = result    
    

