
def alph(c):
    if c >= 'a':
        return ord(c) - ord('a')
    return ord(c) - ord('A')


def firstUnrepeatedStringEnds(digit):
    dic = [-1 for x in range(27)]

    left = 0
    i = 0
    while (i < len(line) and i-left < digit):
        c = line[i]
        last = dic[alph(c)]
        if (left <= last):
            left = last + 1
        dic[alph(c)] = i
        i += 1
    
    return i

with open("day6.txt") as f:
    line = f.readlines()[0]
    
    print(firstUnrepeatedStringEnds(4))
    print(firstUnrepeatedStringEnds(14))