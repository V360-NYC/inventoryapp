from queryParsing import *
from utils import *
import pandas as pd

def dict2df(searchResult):
    data=[searchResult[str(a)] for a in range(1,len(searchResult))]
    df=pd.DataFrame.from_dict(data)
    df.columns=searchResult['0']
    return df

def changeColumnVisibility(lastResult,uid, queryMode, ts, columnNameArray, showBool):
    shownColumnName = lastResult["columnName"]
    newShownColumnName = []
    newHiddenColumnName = []
    if (showBool):
        newShownColumnName = shownColumnName
        for i in range(len(lastResult["hiddenColumnName"])):
            if indexOf(columnNameArray,lastResult["hiddenColumnName"][i]) != -1:
                newShownColumnName.append(lastResult["hiddenColumnName"][i])
            else:
                newHiddenColumnName.append(lastResult["hiddenColumnName"][i])
    else:
        newHiddenColumnName = lastResult["hiddenColumnName"]
        for i in range(len(lastResult["columnName"])):
            if indexOf(columnNameArray,lastResult["columnName"][i]) != -1:
                newHiddenColumnName.append(lastResult["columnName"][i])
            else:
                newShownColumnName.append(lastResult["columnName"][i])

    #making change in dataframe
    df = lastResult["searchResult"]
    df = dict2df(df)
    resultArray = df[newShownColumnName]
    return resultArray
    #cross check with frontend requirements
    #replyUser_(uid, queryMode, ts, 'Search Result', 'Modified table is as follow:', resultArray)
    #saveLastResult_(uid, queryMode, ts, lastResult["searchResult"], lastResult["entityName"], lastResult["entityValue"],newShownColumnName, newHiddenColumnName)

def changeRateLastResult_(lastResult,uid, queryMode, ts, percent, constDollar):
    df = dict2df(lastResult["searchResult"])
    changedRateData = ChangeRateUS(df, percent, constDollar)
    resultArray = ParseBQResultAndCreateArray(changedRateData, lastResult["columnName"])
    return resultArray
	#replyUser_(uid, queryMode, ts, 'Search Result', 'Modified table is as follow:', resultArray)
	#saveLastResult_(uid, queryMode, ts, changedRateData, lastResult["entityName"], lastResult["entityValue"],lastResult["columnName"], lastResult["hiddenColumnName"])
