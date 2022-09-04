from collections import deque
a, b, n, m = map(int, input().split())
stone = [0] * 100001
# 정확한 방문 처리를 위해 초기값을 1로 하고 추후에 결과값 - 1 하거나 
# 애초에 리스트 전체를 -1로 하고 초기값을 0으로 하는 방법도 있음
stone[n] = 1
queue = deque([n])
while True:
    x = queue.popleft()
    # 도착했다
    if x == m:
        print(stone[x] - 1)
        break
    # 8가지 경우의 수
    for i in [x + 1, x - 1, x + a, x - a, x + b, x - b, x * a, x * b]:
        # 돌다리 범위 안에 있고 한번도 방문하지 않았다
        if 0 <= i <= 100000 and stone[i] == 0:
            stone[i] = stone[x] + 1
            queue.append(i)
