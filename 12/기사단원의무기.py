def yaksu(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 2
    if i == n ** 0.5:
        count -= 1
    return count


# def solution(number, limit, power):
#     total = 0
#     for i in range(1, number + 1):
#         if yaksu(i) > limit:
#             total += power
#         else:
#             total += yaksu(i)
#     return total

for i in range(1, 11):
    print(yaksu(i))