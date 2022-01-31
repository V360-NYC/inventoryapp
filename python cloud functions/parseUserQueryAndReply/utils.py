#can be optimize using pandas inbuilt
import pandas as pd
import openpyxl

def dict2df(searchResult):
    data=[searchResult[str(a)] for a in range(1,len(searchResult))]
    df=pd.DataFrame.from_dict(data)
    df.columns=searchResult['0']
    return df
    
def ChangeRateUS(df,percent,constDollar):
    #print(df[['Total','Per','Price/Cts']])
    rateMultiplier = 1.0 + percent*1.0/100
    if len(df)>0:
        for i in range(len(df)):
            if not pd.isnull(df['Total'][i]):
                df.at[i,'Total'] = df['Total'][i] * rateMultiplier + round(constDollar,0)
                df.at[i,'Per'] = 100 - rateMultiplier * round((100 - df['Per'][i]),2) # Need to also consider const for back calculation.
                df.at[i,'Price/Cts'] = round(df['Total'][i]*1.0/df['Size'][i],0)
    #print(df[['Total','Per','Price/Cts']])
    return df

def ParseBQResultAndCreateArray(df,shownColumnName):
    data = []
    if len(df)>0:
        headerRow = shownColumnName
        data.append(headerRow)

        for i in range(len(df)):
            values = []
            for j in range(len(headerRow)):
                if df[headerRow[j]][i]:
                    values.append(df[headerRow[j]][i])
                else:
                    values.append("NA")
            data.append(values)
        #print(data)
    return data

def dataframeToDictionary(df):
    dictionary = dict()
    dictionary['0']=df.columns.values
    for i in range(len(df)):
        dictionary[str(i+1)]=df.iloc[i].values
    return dictionary
