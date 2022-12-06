win = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

lose = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

scoreBoard = {
    'A': 1,
    'B': 2,
    'C': 3
}

with open("day2.txt") as f:
    lines = f.readlines()
    score = 0
    for line in lines:
        oppo = line[0]
        result = line[2]
        
        if (result == 'X'):
            score += scoreBoard[lose[oppo]]
        elif (result == 'Y'):
            score += scoreBoard[oppo] + 3
        else:
            score += scoreBoard[win[oppo]] + 6

    print(score)