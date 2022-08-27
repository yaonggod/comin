# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWVWgkP6sQ0DFAUO&categoryId=AWVWgkP6sQ0DFAUO&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

t = int(input())
for x in range(1, t + 1):
    board = []
    # 옆으로 읽어나가기 위해 단어들의 최대 길이를 구하기
    max_length = 0
    for _ in range(5):
        lst = list(input())
        board.append(lst)
        if len(lst) > max_length:
            max_length = len(lst)
            
    answer = ''
    for i in range(max_length):
        for j in range(5):
            # 좌표에 값이 있으면 넣고, 아님 말고
            try:
                answer += board[j][i]
            except:
                pass
    print('#{}'.format(x), answer)