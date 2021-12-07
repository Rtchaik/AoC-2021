from collections import Counter


def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parseData(myFile):
    return dict(Counter(map(int, open(myFile).read().split(','))))


def part1(data):
    return search(data, lambda x: x)


def part2(data):
    return search(data, lambda x: x * (x + 1) // 2)


def search(data, fun):
    min_pos = min(data)
    max_pos = max(data)
    min_fuel = fuel(data, min_pos, fun)
    max_fuel = fuel(data, max_pos, fun)
    while min_pos - max_pos:
        if min_fuel < max_fuel:
            max_pos = (max_pos + min_pos) // 2
            max_fuel = fuel(data, max_pos, fun)
        else:
            min_pos = (max_pos + min_pos + 1) // 2
            min_fuel = fuel(data, min_pos, fun)
    return min_fuel


def fuel(swarm, pos, fun):
    return sum(fun(abs(k - pos)) * v for k, v in swarm.items())


# def search_brute(data, fun):
#     return min(fuel(data, pos, fun) for pos in range(min(data), max(data) + 1))
