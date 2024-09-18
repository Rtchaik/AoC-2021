def solveDay(myFile):
    data = parseData(myFile)
    levels = {(len(data[0]) - 1, len(data) - 1): 0}
    #print(data,levels)
    print('Part 1: ', part1(levels, data))
    #print('Part 2: ', part2(data))


def parseData(myFile):
    with open(myFile) as f:
        return [line.strip() for line in f.readlines()]


def part1(levels, data, start=(0, 0), last=(0, 0)):
    try:
        return levels[start]
    except KeyError:
        x, y = start
        neighbours = {(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)} - {last}
        valid = [
            point for point in neighbours
            if all(0 <= coord < len(data) for coord in point)
        ]
        levels[start] = min(
            int(data[coord[1]][coord[0]]) + part1(levels, data, coord, start)
            for coord in valid)
        return levels[start]


def part2(data):
    windows = [sum(data[idx:idx + 3]) for idx in range(len(data) - 2)]
    return part1(windows)
