import pandas as pd
from utils import *

map = getMap()
# print(map.keys()) # Output: ['V', '"00"', '"01"', '"11"', '"10"']

# Todo: input
variables = 3
nameVariables = ['A', 'B', 'C', 'D']
groups = calcNumberOfGroups(variables)

lines = [list(map.to_numpy()[i])[1:] for i in range(len(map['V']))]

index = 2 ** (variables / 2) if variables % 2 == 0 else 2 ** ((variables-1) / 2)
linesUsed = lines[0: int(index)]


def position2string(position):
    # position = [[0, 0], [0, 1]]
    stringsPerPosition = []
    for i in range(len(position)):
        # Dps tem que adaptar para mais variáveis
        first = '-A' if position[i][0] == 0 else 'A'
        second = '-B' if position[i][1] < 2 else 'B'
        third = '-C' if position[i][1] == 0 or position[i][1] == 3 else 'C'
        stringsPerPosition.append([first, second, third])

    preString = ''
    for i in range(len(stringsPerPosition[0])):
        if stringsPerPosition[0][i] == stringsPerPosition[1][i]:
            if (len(stringsPerPosition) > 2):
                next = False
                for x in range(2, len(stringsPerPosition)):
                    if stringsPerPosition[0][i] == stringsPerPosition[x][i]:
                        next = True
                        # preString += stringsPerPosition[0][i]
                    else:
                        next = False
                    
                    if next and x == len(stringsPerPosition) - 1:
                        preString += stringsPerPosition[0][i]
            else:
                preString += stringsPerPosition[0][i]
        else:
            pass

    string = preString

    return string


def main(groups):
    groupsOfMap = []
    groupsPerPosition = []
    for index in range(len(groups)):
        group = groups[index]
        initialPositions = []
        if (index == 0):
            if linesUsed[0][0] == 1:
                initialPositions.append({"x": 0, "y": 0})
        else:
            for y in range(len(linesUsed)):
                for x in range(len(linesUsed[y])):
                    if linesUsed[y][x] == 1:
                        initialPositions.append({"x": x, "y": y})

                        
        for initialPosition in initialPositions:
            if (group != 1):

                groupsOfPositions = callIf(initialPosition, group, linesUsed, groupsPerPosition, index)
                if len(groupsOfPositions) > 0:
                    for groupOfPositions in groupsOfPositions:
                        groupsPerPosition.append(groupOfPositions)
                        # groupsOfMap.append(position2string(groupOfPositions))
                else:
                    pass
            else:
                pass
    print(groupsPerPosition)
    return groupsOfMap

                

groupsKarnaugh = main(groups)
print(groupsKarnaugh)
