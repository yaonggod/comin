def gcd(n, m):
    i = min(n, m)
    while True:
        if n % i == 0 and m % i == 0:
            break
        i -= 1
    return i

T = int(input())
for test_case in range(1, T + 1):
    s, t = map(str, input().split())
    n, m = len(s), len(t)
    g = gcd(n, m)
    print(s * (m // g), t * (n // g)) 
    if s * (m // g) == t * (n // g):
        print('{} {}'.format(test_case, 'yes'))
    else:
        print('{} {}'.format(test_case, 'no'))