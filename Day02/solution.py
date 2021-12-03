from collections import defaultdict


def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parseData(myFile):
    with open(myFile) as f:
        return [((instr:=line.split())[0], int(instr[1])) for line in f.readlines()]


def part1(data):
    depth = 0
    horizon = 0
    vertical = {'down':1, 'up':-1}
    for k,v in data:
      if k == 'forward':
        horizon +=v
      else:
        depth+=v*vertical[k]
    return depth*horizon


def part2(data):
    depth = 0
    horizon = 0
    aim = 0
    vertical = {'down':1, 'up':-1}
    for k,v in data:
      if k == 'forward':
        horizon +=v
        depth+=v*aim
      else:
        aim+=v*vertical[k]
    return depth*horizon
