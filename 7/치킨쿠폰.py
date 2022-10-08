def solution(chicken):
    coupon = chicken
    count = 0
    
    while coupon // 10 != 0:
        count += coupon // 10
        coupon += coupon // 10 - (coupon // 10) * 10
        
    return count

print(solution(100))