import unittest
from distance import CalcDistance

class TestGeoData(unittest.TestCase):
    def test_openGeoData(self):
        calcDistance = CalcDistance()
        self.assertIsInstance(calcDistance.geoData,list)
        self.assertGreater(len(calcDistance.geoData),0)
        self.assertIsInstance(calcDistance.geoData[0],dict)
        self.assertIn('id',calcDistance.geoData[0])
        self.assertIn('lnglat',calcDistance.geoData[0])

    def test_IDList(self):
        calcDistance = CalcDistance()
        self.assertEqual(calcDistance.IDList[0],1101)
    
    def test_coordinate(self):
        calcDistance = CalcDistance()
        x,y = calcDistance.coordinate(1101)
        self.assertAlmostEqual(x,141.340956,delta=1e-1)
        self.assertAlmostEqual(y,43.05546,delta=1e-1)
    
    def test_calcBetweenChitose(self):
        calcDistance = CalcDistance()
        ans = calcDistance.calcBetweenChitose(1101)
        self.assertAlmostEqual(ans,36000,delta=1000)
    
    def test_betweenChitose(self):
        calcDistance = CalcDistance()
        for i in [1101,1102,1101,1104,1204]:
            ans = calcDistance.betweenChitose(i)
        
if __name__ == "__main__":
    unittest.main()
