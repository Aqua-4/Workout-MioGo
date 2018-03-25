import os
import json
import operator
import pandas as pd

URL = "C:\\Users\\Parashar\\Desktop\\workspace\\Extract Workout csv.csv"


DF = pd.read_csv(URL,'r',delimiter= ',' ,encoding="utf-8")


def etl_func(df):
    df = df[[' starttime', ' runningtime', ' spdavg', ' hravg']]

    df = df[df[" runningtime"] != '0']
    x= df[df[' hravg'] !=  ' manual_dist(12s)'] 
    cleanDF =x[df[' hravg'] !=  ' hravg']
    cleanDF=cleanDF.reset_index(drop = True)
    cleanDF.columns = ["Start-Time","Running-Time", "Speed-Avg","HR-Avg"]
    
    tmpDF = cleanDF['Start-Time'].str.split(' ',expand=True)
    del tmpDF[0]
    tmpDF.columns = ["Start-Date","Start-Time"]
    intDF=cleanDF[["HR-Avg","Speed-Avg"]].astype('int32')
    dateDF=(pd.to_datetime(tmpDF['Start-Date']))
    sTimeDF=(pd.to_timedelta(tmpDF['Start-Time']))
    timeDF=(pd.to_timedelta(cleanDF['Running-Time']))
    cleanDF = pd.concat([dateDF,sTimeDF,timeDF,intDF],axis=1)
    

#     print(cleanDF)
    return cleanDF
    
df = etl_func(DF)
print(df)

