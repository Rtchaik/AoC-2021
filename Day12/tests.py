import Day12.solution as current

test1 = {'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'c': ['A'], 'b': ['A', 'd', 'end'], 'd': ['b']}

assert current.part1(test1) == 10

assert current.part2(test1) == 36