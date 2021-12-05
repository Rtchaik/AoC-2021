import Day05.solution as current
import numpy as np

test1 = [[0, 9, 5, 9], [8, 0, 0, 8], [9, 4, 3, 4], [2, 2, 2, 1], [7, 0, 7, 4], [6, 4, 2, 0], [0, 9, 2, 9], [3, 4, 1, 4], [0, 0, 8, 8], [5, 5, 8, 2]]

test_ocean = np.zeros((10,10))

assert current.part1(test1,test_ocean ) == 5

assert current.part2(test1, test_ocean) == 12