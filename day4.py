def takeFirst(elem):
    return elem[0]

with open("day4.txt") as f:
    lines = f.readlines()
    count = 0

    for line in lines:
        schedule = [[int(y) for y in x.split('-')] for x in line.split(',')]
        schedule.sort(key=takeFirst)
        
        if (schedule[0][1] >= schedule[1][0]):
            count += 1
    
    print(count)