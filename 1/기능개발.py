# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    n = len(progresses)
    done = [False] * n
    result = []
    patch = 0
    while True:
        patch = 0
        # 모든 패치가 완료되었을 시 빠져나옴
        if done == [True] * n:
            break
        # done_previous = done 하면 done_previous도 변하게 됨
        done_previous = done[:]
        # 하루동안 작업 진핻
        for i in range(n):
            progresses[i] += speeds[i]
        # 작업 진행 후 100을 넘으면 done
        for i in range(n):
            if progresses[i] >= 100:
                done[i] = True
        # 작업을 진행해서 완성된 작업이 추가가 되었다
        if done_previous != done:
            # print(done_previous)
            # print(done)
            # 첫 작업부터 연속적으로 완성된 작업을 세 주고, 도중에 미완성된 작업이 있으면 끊어줌
            for i in range(n):
                if done[i] == True:
                    patch += 1
                else:
                    break
            # print(patch)
            # 기존의 패치 목록에서 추가된 것이 있다
            if patch - sum(result) > 0:
                result.append(patch - sum(result))
    
    return result
            