import Day09.solution as current

test1 = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0], [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
         [9, 8, 5, 6, 7, 8, 9, 8, 9, 2], [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
         [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]

result = current.part1(test1)

assert result[1] == 15

assert current.part2(test1, result[0]) == 1134
