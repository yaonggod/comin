import itertools

def solution(original_orders, course):
    # 모든 주문들을 알파벳 순으로 재정렬해야 조합에서 중복되는 조합이 안나옴
    orders = []
    for order in original_orders:
        orders.append(''.join(sorted(list(order))))
        
    orders.sort(key = lambda x : len(x))

    # 메뉴들에서 나올 수 있는 모든 조합
    combs = []
    for order in orders:
        for j in course:
            if len(order) >= j:
                for comb in itertools.combinations(order, j):
                    if [comb, 0] not in combs:
                        # 조합, 조합이 나온 횟수
                        combs.append([comb, 0])
    combs.sort(key = lambda x : len(x[0]))
    
    # 각 조합이 몇 번 나왔는지 세기
    for order in orders:
        for comb in combs:
            if len(comb[0]) <= len(order):
                for letter in comb[0]:
                    if letter not in order:
                        break
                else:
                    comb[1] += 1
    # 조합 길이마다 최대 출현 횟수를 세고, 최대 출현 횟수가 2 이상이면 메뉴 조합으로 인정
    result = []
    for j in course:
        lst = []
        for comb in combs:
            if len(comb[0]) == j:
                lst.append(comb)
        max_result = 0
        for c in lst:
            if c[1] > max_result:
                max_result = c[1]
        for c in lst:
            if c[1] == max_result and max_result > 1:
                result.append(''.join(c[0]))
    
    return sorted(result)    

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
        
            


      

    
            
    
    
    



    
            
    
        
            
            
            
        
    
    


             
            
            
    
    
    
    


            
                    

        
    
        
        
        

           
    
        
        
    
        
    
        
    