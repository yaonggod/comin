# https://school.programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    arr = [[' '] * n for _ in range(n)]
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if arr1[i] // (2 ** j) == 1:
                arr[i][n - 1 - j] = '#'
                arr1[i] -= 2 ** j
                
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if arr2[i] // (2 ** j) == 1:
                arr[i][n - 1 - j] = '#'
                arr2[i] -= 2 ** j
    
    answer = []
    for x in arr:
        answer.append(''.join(x))
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))