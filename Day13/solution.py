def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', len(part1(data[0],data[1][0])))
    print()
    part2(*data)


def parseData(myFile):
    dots,folds = open(myFile).read().split('\n\n')
    dots = {tuple(int(x) for x in dot.split(',')) for dot in dots.split()}
    folds = [[(x:=line.split()[-1].split('='))[0],int(x[1])] for line in folds.splitlines()]
    return dots,folds


def part1(dots, fold):
    new = set()
    for dot in dots:
      if fold[0]=='x':
        new.add((dot[0] if dot[0]<fold[1] else fold[1]*2-dot[0],dot[1]))
      else:
        new.add((dot[0],dot[1] if dot[1]<fold[1] else fold[1]*2-dot[1]))
    return new


def part2(dots, folds):
    for fold in folds:
      dots = part1(dots,fold)
    maxes = ([max(x)+1 for x in zip(*dots)])
    code = [['.' for x in range(maxes[0])] for y in range(maxes[1])]
    for dot in dots:
      code[dot[1]][dot[0]]='#'
    for line in code:
      print(''.join(line))