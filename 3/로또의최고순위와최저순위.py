# https://school.programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    zeros = lottos.count(0)
    count = 0
    for n in lottos:
        if n in win_nums:
            count += 1
    result_max = 7 - zeros - count
    result_min = 7 - count
    result = []
    if result_max == 7:
        result.append(6)
    else:
        result.append(result_max)
    if result_min == 7:
        result.append(6)
    else:
        result.append(result_min)
    return result

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))