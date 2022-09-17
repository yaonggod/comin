import sys
input = sys.stdin.readline

t = int(input())
for x in range(1, t + 1):
    n = int(input())
    lst = list(map(str, input().split()))
    sum_ = 0
    for number in lst:
        sum_ += int(number[:-1]) ** int(number[-1])
    print('#{} {}'.format(x, sum_))
    