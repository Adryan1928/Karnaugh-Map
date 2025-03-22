import pandas as pd
def getMap():
    try:
        mapExcel = pd.read_excel("Map.xlsx", sheet_name="Planilha1")
        map= pd.DataFrame(mapExcel)
        return map
    except:
        return "Error"

def calcNumberOfGroups(variables):
    groups = []
    for i in range(variables + 1):
        groups.append(2**i)
    groups.sort(reverse=True)
    return groups

def positionsIf(positions, linesUsed):
    isTrue = True

    for position in positions:
        if linesUsed[position["y"]][position["x"]] == 0:
            isTrue = False
            break
    return isTrue

def calcPositions(initialPositionRelative, group, numColumns):
    positions = [initialPositionRelative]
    print("initialPositionRelative", initialPositionRelative, group)
    for i in range(1, group):
        print("i", i)
        if (initialPositionRelative["x"] + group <= numColumns):
            x = initialPositionRelative["x"] + i
        else:
            if (initialPositionRelative["x"] + i < numColumns):
                x = initialPositionRelative["x"] + i
            else:
                x = initialPositionRelative["x"] + i - numColumns
        y = initialPositionRelative["y"]
        positions.append({"x": x, "y": y})
    print("positions", positions)
    return positions

def existsInGroup(groupsPerPosition, groupPossibilities):
    exists = True
    for position in groupPossibilities:
        existsInPosition = False
        for groupOld in groupsPerPosition:
            if position in groupOld:
                existsInPosition = True
                break
        if not existsInPosition:
            exists = False
            break
            
    return exists

def callIf(initialPosition, group, linesUsed, groupsPerPosition, index):
    numColumns = len(linesUsed[0]) # X
    numLines = len(linesUsed) # Y
    groupsPossibilities = [] # Somente de uma posição inicial

    # Tem que reavaliar para casos com mais de 4 variáveis
    possibilities = 2
    if numColumns == group/2:
        possibilities = 1
    else: 
        if group == 4 and index == 2:
            possibilities += 1
            


    for x in range(possibilities):
        groupsPerPossibility = [] # Somente de uma posição inicial e direção
        if index == 0:
            for i in range(numLines): #Preciso disso para chamar o positionsIf
                initialPositionRelative = {"x": 0, "y": i}
                positions = calcPositions(initialPositionRelative, int(group/2), numColumns)
                if positionsIf(positions, linesUsed):
                    groupsPerPossibility.append(positions)
            
            if (len(groupsPerPossibility) == numLines):
                groupFixed = []
                for groupPerPossibility in groupsPerPossibility:
                    for position in groupPerPossibility:
                        groupFixed.append(position)

                groupsPossibilities.append(groupFixed)
        else:
            breakline = 2 ** x

            if (breakline + initialPosition["y"] <= numLines):
                for newLine in range(breakline):

                    initialPositionRelative = {"x": initialPosition["x"], "y": initialPosition["y"] + newLine}
                    positions = calcPositions(initialPositionRelative, int(group/breakline), numColumns)
                    if positionsIf(positions, linesUsed):
                        groupsPerPossibility.append(positions)
                
                if (len(groupsPerPossibility) == breakline):
                    groupFixed = []
                    for groupPerPossibility in groupsPerPossibility:
                        for position in groupPerPossibility:
                            groupFixed.append(position)

                    groupsPossibilities.append(groupFixed)
    finalGroups = []
    for groupPossibility in groupsPossibilities:
        if not existsInGroup(groupsPerPosition, groupPossibility):
            finalGroups.append(groupPossibility)
    
    return finalGroups