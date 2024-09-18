def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data))
    # print('Part 2: ', part2(data))


def parseData(myFile):
    return open(myFile).readline()


def part1(data):
    return ''.join(bin(int(ch, 16))[2:].zfill(4) for ch in data)


def part2(data):
    windows = [sum(data[idx:idx + 3]) for idx in range(len(data) - 2)]
    return part1(windows)
