from collections import Counter, defaultdict


def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parseData(myFile):
    return dict(Counter(map(int, open(myFile).read().split(','))))


def part1(data):
    return sum(breeding(data, 80).values())


def part2(data):
    return sum(breeding(data, 256).values())


def breeding(swarm, days):
    while days:
        new = defaultdict(int)
        for k, v in swarm.items():
            if k > 0:
                new[k - 1] += v
            else:
                new[6] += v
                new[8] += v
        swarm = new
        days -= 1
    return swarm
