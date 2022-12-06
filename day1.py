res = []
curr = 0
with open('day1.txt') as f:
    lines = f.readlines()
    for line in lines:
        if (line == "\n"):
            res.append(curr)
            curr = 0
        else:
            curr += int(line)
res.append(curr)

res.sort(reverse = True)

print(res[0])
print(sum(res[0:3]))