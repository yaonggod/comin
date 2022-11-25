word = input()
result = ''
i = 0
while i < len(word):
    while True:
        if word[i] == 'U':
            result += 'U'
            break
        i += 1
    if result == 'U':
        print(i)
        break
i += 1
while i < len(word):
    while True:
        if word[i] == 'C':
            result += 'C'
            break
        i += 1
    if result == 'UC':
        print(i)
        break
i += 1
while i < len(word):
    while True:
        if word[i] == 'P':
            result += 'P'
            break
        i += 1
    if result == 'UCP':
        print(i)
        break
i += 1
while i < len(word):
    while True:
        if word[i] == 'C':
            result += 'C'
            break
        i += 1
    if result == 'UCPC':
        print(i)
        break
if result == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')
