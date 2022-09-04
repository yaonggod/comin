def solution(id_list, report, k):
    # 리폿 결과는 중복 인정하지 않음
    report = list(set(report))
    
    # 각 유저가 리폿당한 횟수 입력
    dict_report = {}
    for i in range(len(report)):
        a, b = report[i].split()
        if b not in dict_report:
            dict_report[b] = 1
        else:
            dict_report[b] += 1
    # 최종 리폿될 유저
    report_list = []
    for r in dict_report:
        if dict_report[r] >= k:
            report_list.append(r)
    # 리폿 결과 메일로 보내기
    answer = [0 for _ in range(len(id_list))]
    for i in range(len(report)):
        a, b = report[i].split()
        if b in report_list:
            answer[id_list.index(a)] += 1
    
    return answer