# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    test_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(survey)):
        # 왼쪽 유형에 가깝다
        if choices[i] <= 3:
            test_dict[survey[i][0]] += 4 - choices[i]
        # 오른쪽 유형에 가깝다
        elif choices[i] >= 5:
            test_dict[survey[i][1]] += choices[i] - 4
    # 점수가 동일한 경우 사전순으로 앞서는 알파벳이 result에 들어감
    result = ''
    if test_dict['R'] >= test_dict['T']:
        result += 'R'
    else:
        result += 'T'
        
    if test_dict['C'] >= test_dict['F']:
        result += 'C'
    else:
        result += 'F'
    
    if test_dict['J'] >= test_dict['M']:
        result += 'J'
    else:
        result += 'M'
    
    if test_dict['A'] >= test_dict['N']:
        result += 'A'
    else:
        result += 'N'
        
    return result