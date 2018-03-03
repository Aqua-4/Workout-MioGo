import os
import json
import operator
import pandas as pd

URL = "C:\\Users\\Parashar\\Desktop\\workspace\\Extract Workout csv.csv"

DF = pd.read_csv(URL,'r',delimiter= ',' ,encoding="utf-8")

print(DF.columns)

df = df[[' starttime', ' runningtime', ' spdavg', ' hravg']]
# colunm names need to be renamed properly

df = df[df[" runningtime"] != '0']

print(df)
# df ROWS-2 needs to be joined with some rollover function  
