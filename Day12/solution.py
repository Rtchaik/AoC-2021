from collections import defaultdict


def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parseData(myFile):
    connect = defaultdict(list)
    with open(myFile) as f:
        for line in f.readlines():
            pair = line.strip().split('-')
            for p1, p2 in zip(pair, reversed(pair)):
                if p2 != 'start':
                    connect[p1].append(p2)
        del connect['end']
        return connect


def part1(data, path=['start']):
    final = 0
    for point in data[path[-1]]:
        if point.isupper() or not point in path:
            final += 1 if point == 'end' else part1(data, path + [point])
    return final


def part2(data, path=['start']):
    final = 0
    for point in data[path[-1]]:
        final += 1 if point == 'end' else (part2,
                                           part1)[point.islower()
                                                  and point in path](
                                                      data, path + [point])
    return final
