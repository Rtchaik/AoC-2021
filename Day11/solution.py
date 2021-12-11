import numpy as np


def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data, 100))
    print('Part 2: ', part2(data))


def parseData(myFile):
    return np.array([[int(num) for num in line.strip()]
                     for line in open(myFile).readlines()])


def part1(data, steps, flash=0):
    while steps:
        data, flash = make_step(data, flash)
        steps -= 1
    return flash


def part2(data):
    steps = 0
    while len(data[data == 0]) < 100:
        data = make_step(data, 0)[0]
        steps += 1
    return steps


def make_step(data, flash):
    data = data + 1
    while len(data[data > 9]):
        for x in range(10):
            for y in range(10):
                if data[y, x] > 9:
                    data[y, x] = 0
                    flash += 1
                    for neighbour in neighbours((y, x)):
                        if data[neighbour] != 0:
                            data[neighbour] += 1
    return data, flash


def neighbours(point):
    return set.union(*[{(y, x)
                        for x in
                        (point[1] - 1, point[1], point[1] + 1) if 0 <= x < 10}
                       for y in (point[0] - 1, point[0], point[0] + 1)
                       if 0 <= y < 10]) - {point}
