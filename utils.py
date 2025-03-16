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

# def getGroups(map, groups):
#     notA = map.loc[0].values
#     print(notA)