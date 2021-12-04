def solveDay(myFile):
    data = parseData(myFile)
    game = bingo(data)
    print('Part 1: ', game[0])
    print('Part 2: ', game[-1])


def parseData(myFile):
    with open(myFile) as f:
        draws = list(reversed(f.readline().strip().split(',')))
        raw_boards = list(reversed(f.readlines()))
        boards = []
        for group in range(len(raw_boards) // 6):
            raw_boards.pop()
            board = []
            for _ in range(5):
                board.append(raw_boards.pop().split())
            boards.append(board + list(zip(*board)))
        boards = [[set(line) for line in board] for board in boards]
        return draws, boards


def bingo(data):
    marked = set()
    scores = []
    while data[1]:
        win = []
        current = data[0].pop()
        marked |= {current}
        for board in data[1]:
            for line in board:
                if line <= marked:
                    scores.append(
                        int(current) *
                        sum(int(item) for item in set.union(*board) - marked))
                    win.append(board)
                    break
        if win:
            for board in win:
                data[1].remove(board)
    return scores
