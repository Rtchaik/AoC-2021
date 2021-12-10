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
    scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    result = []
    for line in lines:
        points = 0
        for ch in reversed(line):
            points = points * 5 + scores[ch]
        result.append(points)
    final = sorted(result)
    return final[len(final) // 2]
