import pandas as pd
from utils import *

map = getMap()
# print(map.keys()) # Output: ['A - B/C', '"00"', '"01"', '"11"', '"10"']

variables = 3
nameVariables = ['A', 'B', 'C']
groups = calcNumberOfGroups(variables)



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


def getGroups(groups):
    notA = map.loc[0].values[1:]
    yesA = map.loc[1].values[1:]
    print(notA)
    print(yesA)

    groupsOfMap = []

    for i in range(groups[0]):
        groupInTurn = False
        for x in range(2):
            if i < groups[0]/2:
                initialPosition = [0, i]
            else:
                initialPosition = [1, i-groups[0]/2]
        next = True
        while next:

            # Verificar notA or yesA
            if initialPosition[0] == 0:
                if notA[initialPosition[1]] == 1:
                    if initialPosition[1] != len(notA) - 1:
                        if notA[initialPosition[1] + 1] == 1:
                            groupInTurn = True
                            print("oi")
                            string = position2string([initialPosition,
                            [initialPosition[0], initialPosition[1] + 1]])
                            groupsOfMap.append(string)

                            if notA[initialPosition[1] + 2] == 1:
                                print("True??")
                                pass
                            else:
                                # Verificar para baixo
                                print('False')
                                next = False
                                break

                        else:
                            # Verificar para baixo
                            next = False
                    else:
                        # Verificar se é a última posição, se sim, verificar a primeira e dps para baixo
                        pass
                else:
                    next = False
            else:
                next = False
                pass
        
    return groupsOfMap

                

groupsKarnaugh = getGroups(groups)
print(groupsKarnaugh)
