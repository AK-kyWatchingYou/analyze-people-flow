import pandas as pd

file_path = '/data/2021/PDP_0001_20210801_afternoon.csv'
useCols = ["dailyid","month","day","hour","minute","home_citycode"]

df = pd.read_csv(file_path,encoding="utf-8")

df.to_csv("/data/formated/0801.csv",columns=useCols,index=False)