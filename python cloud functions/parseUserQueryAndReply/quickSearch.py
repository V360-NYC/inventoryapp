import pandas as pd
import numpy as np
import math
import os
import pandasql as ps
from pandasql import sqldf
import json
colorMap={}
colorMap['D']=colorMap['E']=colorMap['F']=0
colorMap['G']=colorMap['H']=1
colorMap['I']=colorMap['J']=2
colorMap['K']=colorMap['L']=colorMap['M']=colorMap['N']=3

clarityMap={

'FL': 0,
'IF': 0,
'VVS1': 1,
'VVS2': 1,
'VS1': 2,
'VS2': 2,
'SI1': 3,
'SI2': 3,
'I1': 4,
'I2': 4,
'I3': 4  
}

def classifyRow_(row):
#     print(row)
    color=row['Color']
    clarity=row['Purity']
    carat=row['Carat']
    colorIdx=3
    if color in colorMap.keys():
        colorIdx=colorMap[color]
    clarityIdx=4
    if clarity in clarityMap.keys():
        clarityIdx=clarityMap[clarity]
    caratIdx=0
    if carat<0.46:
        caratIdx=0
    elif carat<0.96:
        caratIdx=1
    elif carat<1.436:
        caratIdx=2
    else :
        caratIdx=3
    a={}
    a['color']=colorIdx
    a['carat']=caratIdx
    a['clarity']=clarityIdx
    return a

def createQSR(rows):
    quickSearchArray = []
    headerRow = ['color', 'clarity', 'carat']
    colorVal = ['D E F', 'G H', 'I J', 'K L M N']
    clarityVal = ['IF', 'VVS', 'VS', 'SI', 'I']
    caratVal = ['0.18 to 0.45', '0.46 to 0.95', '0.96 to 1.45', '1.46 to 10.0']
    colorValSearch = ['D E F', 'G H', 'I J', 'K L M N']
    clarityValSearch = ['FL IF ', 'VVS1 VVS2', 'VS1 VS2', 'SI1 SI2', 'I1 I3']
    caratValSearch = ['0.18 0.45', '0.46 0.95', '0.96 1.45', '1.46  10.0']
    caratActualVal = [0.18, 0.46, 0.96, 10.0]
    quickSearchArray.append(headerRow)
    quickSearchArray.append(colorVal)
    quickSearchArray.append(clarityVal)
    quickSearchArray.append(caratVal)
    quickSearchArray.append(colorValSearch)
    quickSearchArray.append(clarityValSearch)
    quickSearchArray.append(caratValSearch)
    a3d=[]
    for i in range(4):
        a3d.append([])
        for j in range(5):
            a3d[i].append([])
            for k in range(4):
                a3d[i][j].append([0,1000000,0])

    
#     print(len(a3d))
#     print(len(a3d[0]))
#     print(len(a3d[0][0]))
    for i in range(len(rows)):
        row=rows.iloc[i]
        ct=classifyRow_(row)
        c1=ct['color']
        c2=ct['clarity']
        c3=ct['carat']
#         print('c1 {} c2 {} c3 {}',c1,c2,c3)
        
        a3d[c1][c2][c3][0]=a3d[c1][c2][c3][0]+ row['count']
        if row['Min_price']<a3d[c1][c2][c3][1] and row['Min_price']>10:
            a3d[c1][c2][c3][1]=row['Min_price']
        if row['Max_price']>a3d[c1][c2][c3][2]:
            a3d[c1][c2][c3][2]=row['Max_price']
    ans={}
    stats=a3d

    for i in range(len(stats)):
        for j in range(len(stats[i])):
            for k in range(len(stats[i][j])):
                for l in range(len(stats[i][j][k])):
                    try:
                        stats[i][j][k][l]=stats[i][j][k][l].item()
                    except:
                        pass
    for i in range(len(stats)):
        for j in range(len(stats[i])):
            for k in range(len(stats[i][j])):
                for l in range(len(stats[i][j][k])):
                    try:
                        print(type(stats[i][j][k][l]))
                    except:
                        pass

    
    ans['quickSearchArray']=json.dumps(quickSearchArray)
    ans['stats']=json.dumps(stats)
    return ans
    
    