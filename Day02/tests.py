import Day02.solution as current

test1 = [('forward', 5), ('down', 5), ('forward', 8), ('up', 3), ('down', 8), ('forward', 2)]

assert current.part1(test1) == 150

assert current.part2(test1) == 900