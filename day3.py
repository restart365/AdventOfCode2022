def getOrd(c):
    if c >= 'a':
        return 1 + (ord(c) - ord('a'))
    return 27 + (ord(c) - ord('A'))

# part 1
# with open('day3.txt') as f:
#     lines = f.readlines()

#     res = 0

#     for line in lines:
#         exist = set()
#         lineRes = set()
#         n = len(line)

#         for i in range(int(n/2)):
#             num = getOrd(line[i])
#             exist.add(num)

#         for i in range(int(n/2), n):
#             num = getOrd(line[i])
#             if (num in exist):
#                 lineRes.add(num)

#         res += sum(lineRes)
    
#     print(res)


with open('day3.txt') as f:
    lines = f.readlines()

    res = 0
    i = 0
    while(i < len(lines)):
        set1 = set(lines[i].strip())
        set2 = set(lines[i+1].strip())
        set3 = set(lines[i+2].strip())

        groupRes = list(set1.intersection(set2, set3))
        print(groupRes)
        res += getOrd(groupRes[0])

        i += 3

    print(res)
