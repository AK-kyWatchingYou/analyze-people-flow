import unittest
import pandas as pd
from reformat import Reformat

class TestReformat(unittest.TestCase):
    def test_allFilename(self):
        reformat = Reformat()
        allFilename = reformat.allFilename(dirPath=['/data/2021','/data/2022','/data/2023'])
        self.assertNotEqual(allFilename[0],'/data/2021/PDP_0001_20210801_afternoon.csv')
    
    def test_query(self):
        reformat = Reformat()
        df = pd.read_csv('/data/2021/PDP_0001_20210801_afternoon.csv',encoding="utf-8",usecols=reformat.usecols)
        qf = reformat.query(df,[40,41,140,142])
    
    def test_loadCSV(self):
        reformat = Reformat()
        df = pd.read_csv('/data/2021/PDP_0001_20210801_afternoon.csv',encoding="utf-8",usecols=reformat.usecols)
        reformat.loadcsv(df)
        self.assertAlmostEqual(reformat.dfList[0].iloc[0]['home_citycode'],1222)
        self.assertAlmostEqual(reformat.dfList[0].iloc[0]['distance'],50602)
    

if __name__ == '__main__':
    unittest.main() 
    