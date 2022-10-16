import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t + 1):
    d, h, m = map(int, input().split())
    answer = 0
    answer += (d - 11) * 24 * 60
    answer += (h - 11) * 60
    answer += m - 11
    if answer < 0:
        answer = -1
    print('#{} {}'.format(tc, answer))    
    