from functools import reduce
from operator import mul


def solveDay(myFile):
    data = parseData(myFile)
    result = part1(data)
    print('Part 1: ', result[1])
    print('Part 2: ', part2(data, result[0]))


def parseData(myFile):
    return [[int(n) for n in line.strip()]
            for line in open(myFile).readlines()]


def part1(data):
    max_x = len(data[0])
    max_y = len(data)
    low_points = sum(
        ([(y, x)
          for x in range(max_x) if check_low(data, (y, x), max_x, max_y)]
         for y in range(max_y)), [])
    return low_points, sum(data[p[0]][p[1]] + 1 for p in low_points)


def part2(data, low_points):
    max_x = len(data[0])
    max_y = len(data)
    basins = []
    for point in low_points:
        new = {point}
        basin = set()
        while new:
            basin |= new
            new = set().union(*[set(neighbours(p, max_x, max_y))
                                for p in new]) - basin
            new = {p for p in new if data[p[0]][p[1]] != 9}
        basins.append(len(basin))
    return reduce(mul, sorted(basins, reverse=True)[:3])


def check_low(data, point, max_x, max_y):
    return data[point[0]][point[1]] < min(
        data[n[0]][n[1]] for n in neighbours(point, max_x, max_y))


def neighbours(point, max_x, max_y):
    return [
        (point[0], p) for p in (point[1] - 1, point[1] + 1) if 0 <= p < max_x
    ] + [(p, point[1]) for p in (point[0] - 1, point[0] + 1) if 0 <= p < max_y]
