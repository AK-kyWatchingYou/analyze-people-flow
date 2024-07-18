import os
import pandas as pd
import sys
sys.path.append("/app")
from distance.distance import CalcDistance

class Reformat:
    def __init__(self):
        self.fileList = self.allFilename(dirPath=['/data/2021','/data/2022','/data/2023']) 
        self.usecols = ["dailyid","home_citycode",'latitude','longitude']
        self.dfList = self.emptyDf()
        self.calcDistance = CalcDistance()

        #追記してください

        #[lat1,lat2,lng1,lng2] lat1<latitude<lat2 lng1<longitude<lng2
        self.latlng = []
        #出力ファイル名を定義
        self.outputName = []
    
    def allFilename(self,dirPath):
        li = []
        for d in dirPath:
            dirList = os.listdir(d)
            li.append(dirList)
        res = []
        for i in range(len(li)):
           for l in li[i]:
               res.append(f'/data/{2021 + i}/{l}')     
        return res
    
    def emptyDf(self):
        li = []
        for _ in range(20):
            df = pd.DataFrame(columns=['dailyid', 'latitude', 'longitude','home_citycode','distance'])
            li.append(df)
        return li
    
    
    def query(self,df,latlng):
        #クエリの展開の順番をいじるならここ
        lat1,lat2,lng1,lng2 = latlng
        df = df.dropna()
        qf = df.query('@lat1 < latitude < @lat2 and @lng1 < longitude < @lng2')
        qf = qf.drop_duplicates(subset='dailyid')
        qf['distance'] = qf['home_citycode'].apply(self.calcDistance.betweenChitose)
        return qf
    
    def loopLoadcsv(self):
        for f in self.fileList:
            df = pd.read_csv(f,encoding="utf-8",usecols=self.usecols)
            self.loadcsv(df)
            print(f)
    
    def save(self):
        for i in range(len(self.outputName)):
            self.dfList[i].to_csv(f'/data/reformated/{self.outputName[i]}')
        
    
    def loadcsv(self,df:pd.DataFrame):
        for i in range(len(self.latlng)):
            qf = self.query(df,self.latlng[i]) 
            self.dfList[i] = pd.concat([self.dfList[i], qf],ignore_index=True)

#シャープを外すと実行される
#reformat = Reformat()
#reformat.loopLoadcsv()
#reformat.save()