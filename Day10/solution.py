from functools import reduce


def solveDay(myFile):
    data = parseData(myFile)
    part1_result = part1(data)
    print('Part 1: ', part1_result[0])
    print('Part 2: ', part2(part1_result[1]))


def parseData(myFile):
    with open(myFile) as f:
        return [line.strip() for line in open(myFile).readlines()]


def part1(data):
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    result = 0
    incomplete = []
    for line in data:
        chunks = []
        for ch in line:
            if ch in pairs:
                chunks.append(ch)
            else:
                if ch != pairs[chunks.pop()]:
                    result += scores[ch]
                    chunks = []
                    break
        if chunks:
            incomplete.append(chunks)
    return result, incomplete


def part2(lines):
    final = sorted(
        reduce(lambda points, score: points * 5 + '([{<'.index(score) + 1,
               reversed(line), 0) for line in lines)
    return final[len(final) // 2]
