from timeit import default_timer
from importlib import import_module

currentDay = "05"#str(input("Enter day number: ")).zfill(2)
import_module('Day' + currentDay + '.tests')
currentModule = import_module('Day' + currentDay + '.solution')
startTime = default_timer()
currentModule.solveDay(f'Day{currentDay}/raw.txt')
print('Total time: ', '%6.4f' % (default_timer() - startTime))
