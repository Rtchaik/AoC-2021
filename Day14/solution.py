from collections import defaultdict


def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(*data, 10))
    print('Part 2: ', part1(*data, 40))


def parseData(myFile):
    polymer, rules = open(myFile).read().split('\n\n')
    polymer = {''.join(pair): 1 for pair in zip(polymer[:-1], polymer[1:])}
    rules = dict(pair.split(' -> ') for pair in rules.splitlines())
    rules = {k: [k[0] + v, v + k[1]] for k, v in rules.items()}
    return polymer, rules


def part1(pol, rules, steps):
    for _ in range(steps):
        pol = make_step(pol, rules)
    count = defaultdict(int)
    for k, v in pol.items():
        for ch in k:
            count[ch] += v
    quantities = sorted((item + 1) // 2 for item in count.values())
    return quantities[-1] - quantities[0]


def make_step(polymers, rules):
    new = defaultdict(int)
    for poly, count in polymers.items():
        for rule in rules[poly]:
            new[rule] += count
    return new
