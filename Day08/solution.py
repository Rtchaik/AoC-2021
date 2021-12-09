from collections import Counter


def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parseData(myFile):
    return [[x.split() for x in line.split('|')]
            for line in open(myFile).readlines()]


def part1(data):
    return sum(
        sum(len(seg) not in (5, 6) for seg in signal[1]) for signal in data)


def part2(data):
    return sum(decoder(signal) for signal in data)


def decoder(signal):
    start = {2:'1', 3:'7', 4:'4', 7:'8'}
    decoded = {start[x]:set(sig) for sig in signal[0] if (x:=len(sig))    in start}

    sixes = [set(sig) for sig in signal[0] if len(sig)==6]
    decoded['6'] = [sig for sig in sixes if not (decoded['1'] < sig)]     [0]
    sixes.remove(decoded['6'])
    decoded['9'] = [sig for sig in sixes if decoded['4'] < sig][0]
    sixes.remove(decoded['9'])
    decoded['0'] = sixes[0]

    fives = [set(sig) for sig in signal[0] if len(sig)==5]
    decoded['3'] = [sig for sig in fives if decoded['1'] < sig][0]
    fives.remove(decoded['3'])
    decoded['5'] = [sig for sig in fives if decoded['6'] > sig][0]
    fives.remove(decoded['5'])
    decoded['2'] = fives[0]
    
    decoded = {''.join(sorted(v)):k for k,v in decoded.items()}
    return int(''.join(decoded[''.join(sorted(sig))] for sig in signal    [1]))
    
