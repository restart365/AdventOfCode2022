def getSteps(s):
    x = s.split(" ")
    return [int(x[1]), int(x[3]), int(x[5])]

with open("day5.txt") as f:
    lines = f.readlines()

    # Prep data
    i = 0
    stacks = []
    while (lines[i+1] != '\n'):
        line = lines[i].replace("\n", "")
        j = 0
        while (j*4 < len(line)):
            if (len(stacks) == j):
                stacks.append([])
            if (line[j*4] != ' '):
                stacks[j].append(line[j*4+1])

            j += 1
            
        i += 1

    for x in stacks:
        x.reverse()
    
    # Prep steps
    steps = [getSteps(x) for x in lines[i+2:]]

    # Part 1
    # for step in steps:
    #     while (step[0] > 0):
    #         fromStack = step[1] - 1
    #         toStack = step[2] - 1

    #         item = stacks[fromStack].pop()
    #         stacks[toStack].append(item)
    #         step[0] -= 1

    # Part 2
    for step in steps:
        fromStack = step[1] - 1
        toStack = step[2] - 1

        k = len(stacks[fromStack]) - step[0]

        toMove = stacks[fromStack][k:]
        stacks[fromStack] = stacks[fromStack][:k]
        stacks[toStack].extend(toMove)

    print(stacks)

    # Print result
    res = ""
    for stack in stacks:
        res += stack.pop()
    print(res)
