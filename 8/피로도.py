from itertools import permutations
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    lst = []
    for i in range(n, 0, -1):
        lst += list(permutations(range(n), i))
    
    for comb in lst:
        print(comb)
        k0 = k
        for c in comb:
            if k0 < dungeons[c][0]:
                break
            else:
                k0 -= dungeons[c][1]
            print(k0)
        else:
            answer = len(comb)
            break
    return answer

print(solution(80, [[80, 20], [50, 40], [30, 10]]))