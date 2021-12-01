def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parseData(myFile):
    return tuple(map(int, open(myFile).readlines()))


def part1(data):
    return sum(depth > data[idx] for idx, depth in enumerate(data[1:]))


def part2(data):
    windows = [sum(data[idx:idx + 3]) for idx in range(len(data) - 2)]
    return part1(windows)
