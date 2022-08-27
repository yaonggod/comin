# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    supoja = [0, 0, 0]
    
    # 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
    for i in range(len(answers)):
        if i % 5 == 0 and answers[i] == 1:
            supoja[0] += 1
        if i % 5 == 1 and answers[i] == 2:
            supoja[0] += 1
        if i % 5 == 2 and answers[i] == 3:
            supoja[0] += 1
        if i % 5 == 3 and answers[i] == 4:
            supoja[0] += 1
        if i % 5 == 4 and answers[i] == 5:
            supoja[0] += 1
    
    # 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ... 
    for i in range(len(answers)):
        if i % 2 == 0 and answers[i] == 2:
            supoja[1] += 1
        if i % 8 == 1 and answers[i] == 1:
            supoja[1] += 1
        if i % 8 == 3 and answers[i] == 3:
            supoja[1] += 1
        if i % 8 == 5 and answers[i] == 4:
            supoja[1] += 1
        if i % 8 == 7 and answers[i] == 5:
            supoja[1] += 1
    
    # 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
    for i in range(len(answers)):
        if (i % 10 == 0 or i % 10 == 1) and answers[i] == 3:
            supoja[2] += 1
        if (i % 10 == 2 or i % 10 == 3) and answers[i] == 1:
            supoja[2] += 1
        if (i % 10 == 4 or i % 10 == 5) and answers[i] == 2:
            supoja[2] += 1
        if (i % 10 == 6 or i % 10 == 7) and answers[i] == 4:
            supoja[2] += 1
        if (i % 10 == 8 or i % 10 == 9) and answers[i] == 5:
            supoja[2] += 1
    
    answer = []
    for i in range(3):
        if supoja[i] == max(supoja):
            answer.append(i + 1)
    
    return answer