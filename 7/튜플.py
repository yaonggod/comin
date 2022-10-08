def solution(s):
    s = s.split('},')
    b = []
    for i in s:
        b.append(i.strip('{').strip('}').split(','))
    c = []
    for i in b:
        c.append(list(map(int, i)))
    c.sort(key = lambda x : len(x))
    d = []
    for i in c:
        for j in d:
            i.remove(j)
        d.append(i[0])
    
    return d

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))


    
