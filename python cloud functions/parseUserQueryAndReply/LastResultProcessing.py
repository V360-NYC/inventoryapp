from queryParsing import *
from utils import *
import pandas as pd

def changeColumnVisibility(lastResult,columnNameArray,showBool):
    shownColumnName = lastResult["columnName"] #all columns
    oldHide = lastResult["hiddenColumnName"]
    newHiddenColumnName = []
    if (showBool):
        for i in oldHide:
            if indexOf(columnNameArray,i) == -1:
                newHiddenColumnName.append(i)
    else:
        newHiddenColumnName = lastResult["hiddenColumnName"]
        for i in range(len(lastResult["columnName"])):
            if indexOf(columnNameArray,lastResult["columnName"][i]) != -1:
                newHiddenColumnName.append(lastResult["columnName"][i])
    indexes = []
    for i in newHiddenColumnName:
        indexes.append(indexOf(shownColumnName,i))
    #making change in dataframe   
    return [newHiddenColumnName,indexes]
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
