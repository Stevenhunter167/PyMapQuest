from urllib import request
from urllib import parse
import json

class apiIO:
    def __init__(self, key):
        self.url = None
        self.key = key

    def read(self) -> dict:
        response = request.urlopen(self.url)
        jsonData = json.load(response)
        return jsonData

class apiTripIO(apiIO):  # EX:  apiTripIO(start , end , key).read()
	def __init__(self, start: str, end: str, key: str):
		super().__init__(key)
		link = "http://open.mapquestapi.com/directions/v2/route?"
		query = [('key', key), ("from", start), ('to', end)]
		self.url = link + parse.urlencode(query)

class apiSearchIO(apiIO):
    def __init__(self, latlng: list , keyword: str , key: str , results: int):
        super().__init__(key)
        link = "https://www.mapquestapi.com/search/v4/place?"
        query = [('key', key), ('location' , str(latlng[0]) + ', ' + str(latlng[1])), ('q', keyword) , ('limit' , results) , ('sort' , 'distance')]
        self.url = link + parse.urlencode(query)

class apiGeocodeIO(apiIO):
    def __init__(self , location , key):
        super().__init__(key)
        link = "http://www.mapquestapi.com/geocoding/v1/address?"
        query = [('key', key), ('location' , location)]
        self.url = link + parse.urlencode(query)

class MapQuest:
    def __init__(self , key):
        self.key = key

    @staticmethod
    def generatePair(locations):
        indexlist = []
        for i in range(len(locations)):
            indexlist.append(i)
            if i != 0 and i != len(locations) - 1:
                indexlist.append(i)
        newlist = []
        for i in range(0, len(indexlist), 2):
            newlist.append((indexlist[i], indexlist[i + 1]))
        return newlist

    def totalDistance(self , locations: list) -> float:
        if len(locations) == 0 or len(locations) == 1:
            return 0
        newlist = self.generatePair(locations)
        total = 0
        for i , j in newlist:
            apiData = apiTripIO(locations[i] , locations[j] , self.key).read()
            total += apiData["route"]["distance"]
        return total

    def totalTime(self , locations: list) -> float: #TODO Which time
        if len(locations) == 0 or len(locations) == 1:
            return 0
        newlist = self.generatePair(locations)
        total = 0
        for i , j in newlist:
            apiData = apiTripIO(locations[i] , locations[j] , self.key).read()
            total += apiData['route']['time']
        return total

    def directions(self , locations: list) -> list:
        text = []
        if len(locations) == 0 or len(locations) == 1:
            return text
        indexlist = self.generatePair(locations)
        for i , j in indexlist:
            apiData = apiTripIO(locations[i] , locations[j] , self.key).read()
            for item in apiData['route']['legs'][0]['maneuvers']:
                text.append(item['narrative'])
        return text

    def pointOfInterest(self , locations: str , keyword: str , results: int) -> list:
        geodata = apiGeocodeIO(locations , self.key).read()
        latlng = list(geodata['results'][0]['locations'][0]['latLng'].values())[::-1]
        searchdata = apiSearchIO(latlng , keyword , self.key , results).read()
        return [i['displayString'] for i in searchdata['results']]