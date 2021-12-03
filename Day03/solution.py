from collections import Counter


def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parseData(myFile):
    with open(myFile) as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def part1(data):
    gamma = ''
    epsilon = ''
    for item in zip(*data):
        c = Counter(item).most_common()
        gamma += c[0][0]
        epsilon += c[1][0]
    return int(gamma, 2) * int(epsilon, 2)


def part2(data):
    return rating(data, 1) * rating(data, 0)


def rating(data, mode):
    pos = 0
    while len(data) > 1:
        c = sorted(Counter(list(zip(*data))[pos]).most_common(),
                   key=lambda x: (x[1], x[0]))
        data = [item for item in data if item[pos] == c[mode][0]]
        pos += 1
    return int(data[0], 2)
