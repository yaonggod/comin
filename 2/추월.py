# https://www.acmicpc.net/problem/2002
import sys
input = sys.stdin.readline

n = int(input())
car_in = [input() for _ in range(n)]
car_out = [input() for _ in range(n)]

count = 0
# 들어간 차, 0번째 차는 추월당하지 않으므로 패스
for i in range(1, n):
    # 들어간 차보다 앞에 들어갔던 차
    for j in range(i - 1, -1, -1):
        # 앞에 들어갔던 차보다 먼저 나올 경우
        if car_out.index(car_in[i]) < car_out.index(car_in[j]):
            # 추월차량이다
            count += 1
            break

print(count)
        
    
    
    
    
