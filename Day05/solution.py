import numpy as np
import re

def solveDay(myFile):
    data = parseData(myFile)
    ocean = np.zeros((1000,1000))
    print('Part 1: ', part1(data, ocean))
    print('Part 2: ', part2(data, ocean))


def parseData(myFile):
    with open(myFile) as f:
      data = []
      while (line:=f.readline()):
        data.append([int(num) for num in re.findall('\d+',line)])
      return data


def part1(data, ocean):
    for vent in data:
      if not (vent[0]-vent[2] and vent[1]-vent[3]):
        draw_vents(vent, ocean)
    return len(ocean[ocean>1])


def part2(data, ocean):
    for vent in data:
      if vent[0]-vent[2] and vent[1]-vent[3]:
        draw_vents(vent, ocean)
    return len(ocean[ocean>1])

def draw_vents(vent, ocean):
  x_step = np.sign((vent[0]-vent[2])//-1)
  y_step = np.sign((vent[1]-vent[3])//-1)
  while vent[:2] != vent[2:]:
    ocean[vent[0],vent[1]]+=1
    vent[0]+=x_step
    vent[1]+=y_step
  ocean[vent[2],vent[3]]+=1

