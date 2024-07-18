import json
from haversine import haversine,Unit
import bisect

class CalcDistance:
    def __init__(self):
        with open('city_latlng.json', 'r', encoding='utf-8') as file:
            self.geoData = json.load(file)
            self.IDList = self.genIDList()
            self.calcedDict = {}
            self.calcedID = set()
            
    def genIDList(self)->list[int]:
        li = []
        for g in self.geoData:
            li.append(g['id'])
        return li
    
    def binary_search_bisect(self, target):
        index = bisect.bisect_left(self.IDList, target)
        if index < len(self.IDList) and self.IDList[index] == target:
            return index
        return -1  
    
    def betweenChitose(self,citycode)->int:
        if citycode in self.calcedID:
            return self.calcedDict[citycode]
        else:
            ans = self.calcBetweenChitose(citycode)
            self.calcedID.add(citycode)
            self.calcedDict[citycode] = ans
            return ans

    def calcBetweenChitose(self,citycode)->int:
        x,y = self.coordinate(citycode=citycode)
        ans = self.haversine(x,y,141.650876,42.820958)
        return ans
        
    def coordinate(self,citycode):
        index = self.binary_search_bisect(citycode)
        x,y = self.geoData[index]['lnglat'][0],self.geoData[index]['lnglat'][1]
        return x,y
        
    def haversine(self,y1,x1,y2,x2)->int:
        bsas = (x1, y1)
        paris = (x2, y2)
        distance = haversine(bsas, paris, unit=Unit.METERS)  # メートル単位で距離を計算
        return int(distance)
        
