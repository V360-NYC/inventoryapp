from queryParsing import *
from utils import *
import pandas as pd

def changeColumnVisibility(lastResult,columnNameArray,showBool):
    shownColumnName = lastResult["columnNames"] #all columns
    oldHide = lastResult["hiddenColumnNames"]
    newHiddenColumnName = []
    if (showBool):
        for i in oldHide:
            if indexOf(columnNameArray,i) == -1:
                newHiddenColumnName.append(i)
    else:
        newHiddenColumnName = lastResult["hiddenColumnNames"]
        for i in range(len(lastResult["columnNames"])):
            if indexOf(columnNameArray,lastResult["columnNames"][i]) != -1:
                newHiddenColumnName.append(lastResult["columnNames"][i])
    indexes = []
    for i in newHiddenColumnName:
        indexes.append(indexOf(shownColumnName,i))
    #making change in dataframe   
    return [newHiddenColumnName,indexes]
    #cross check with frontend requirements
    #replyUser_(uid, queryMode, ts, 'Search Result', 'Modified table is as follow:', resultArray)
    #saveLastResult_(uid, queryMode, ts, lastResult["searchResult"], lastResult["entityName"], lastResult["entityValue"],newShownColumnName, newHiddenColumnName)

def changeRateLastResult(lastResult,percent, constDollar):
    df = dict2df(lastResult["searchResult"])
    changedRateData = ChangeRateUS(df, percent, constDollar)
    resultArray = ParseBQResultAndCreateArray(changedRateData, lastResult["columnNames"])
    return resultArray
	#replyUser_(uid, queryMode, ts, 'Search Result', 'Modified table is as follow:', resultArray)
	#saveLastResult_(uid, queryMode, ts, changedRateData, lastResult["entityName"], lastResult["entityValue"],lastResult["columnName"], lastResult["hiddenColumnName"])
