import urllib.request
import time
from json import *

from PIL import ImageFile, Image, ImageTk

from Champion import *
from Summoner import *
from League import *
from RankedStats import *
from GameHistory import *
from GameCurrent import *


#regions = ["BR","EUNE","EUW","KR","LAN","LAS","NA","OCE","RU","TR"]
class RiotAPI:

    def __init__(self, key):
        self.lastAPIcall=0
        self.key = key

    def getRequestData(self, url):
        currentTime = time.time()
        if currentTime - self.lastAPIcall < 1.2:
            time.sleep(currentTime - self.lastAPIcall)
        self.lastAPIcall = time.time()
        req = urllib.request.Request(url)
        site = urllib.request.urlopen(req)
        return (site.read()).decode("utf-8")

    def getStaticRequestData(self, url):
        req = urllib.request.Request(url)
        site = urllib.request.urlopen(req)
        return (site.read()).decode("utf-8")

    def getChampions(self,region):
        data = loads(self.getStaticRequestData("https://global.api.pvp.net/api/lol/static-data/" + region + "/v1.2/champion?api_key=" + self.key))
        return ChampionList(data)

    def getSummonerByName(self,region,summonerName):
        temp = summonerName.lower()
        temp = list(temp)
        while ' ' in temp:
            temp.remove(' ')
        temp = "".join(temp)
        data = loads(self.getRequestData("https://na.api.pvp.net/api/lol/" + region +"/v1.4/summoner/by-name/" + temp + "?api_key=" + self.key))
        return Summoner(data[summonerName])

    def getMatchHistory(self, region, summonerId):
        data = loads(self.getRequestData("https://na.api.pvp.net/api/lol/" + region +"/v2.2/matchhistory/" + str(summonerId) + "?api_key=" + self.key))
        return History(data)

    def getCurrentGame(self,platformID,summonerId):
        data = loads(self.getRequestData("https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/" + platformID + "/" +str(summonerId) + "?api_key=" + self.key))
        return CurrentGame(data)

    def getChampion(self,region,champid):
        data = loads(self.getStaticRequestData("https://global.api.pvp.net/api/lol/static-data/" + region +"/v1.2/champion/" + str(champid) + "?api_key=" + self.key))
        return Champion(data)

    def getLeague(self,region,summonerId):
        data = loads(self.getRequestData("https://na.api.pvp.net/api/lol/"+region+"/v2.5/league/by-summoner/"+str(summonerId)+"?api_key=" + self.key))
        return LeagueList(data[str(summonerId)])

    def getRankedStats(self,region,summonerId):
        data = loads(self.getRequestData("https://na.api.pvp.net/api/lol/"+region+"/v1.3/stats/by-summoner/"+str(summonerId)+"/ranked?season=SEASON2015&api_key=" + self.key))
        return RankedStats(data)

