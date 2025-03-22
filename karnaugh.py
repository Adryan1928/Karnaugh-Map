import pandas as pd
from utils import *

map = getMap()

# Todo: input
variables = int(input('Quantas variáveis? '))
nameVariables = ['A', 'B', 'C', 'D'] # Torna dinâmico para mais variáveis
variablesUsed = nameVariables[:variables]
groups = calcNumberOfGroups(variables)

lines = [list(map.to_numpy()[i])[1:] for i in range(len(map['V']))]

index = 2 ** (variables / 2) if variables % 2 == 0 else 2 ** ((variables-1) / 2)
linesUsed = lines[0: int(index)]

positions1 = calcPositions1(linesUsed)


def main():
    groupsOfMap = []
    groupsPerPosition = []
    for index in range(len(groups) - 1):
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
                        string = position2string(groupOfPositions, variables, variablesUsed)
                        groupsOfMap.append(string)
                        # groupsOfMap.append(position2string(groupOfPositions))
    
    for position in positions1:
        if not existsInGroup(groupsPerPosition, [position]):
            groupsPerPosition.append([position])
            string = position2string([position], variables, variablesUsed)
            groupsOfMap.append(string)
    
    print(groupsPerPosition)
    return groupsOfMap

                

groupsKarnaugh = main()

formula = ''
for i in range(len(groupsKarnaugh)):
    if (i == len(groupsKarnaugh) - 1):
        formula += f'{groupsKarnaugh[i]}'
    else:
        formula += f'{groupsKarnaugh[i]} + '

print(formula)
