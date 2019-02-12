from tkinter import *
from model import *
from urllib.request import *
import urllib.error

from time import sleep

from PIL import ImageFile, Image, ImageTk


class GUIwindow:

    def __init__(self,master,key):
        self.api = RiotAPI(key)

        self.plaformsId = {"br":"BR1","eune":"EUN1","euw":"EUW1","kr":"KR","lan":"LA1","las":"LA2","na":"NA1","oce":"OC1","ru":"RU","tr":"TR1"}
        self.tiers = {"CHALLENGER":"C", "MASTER":"M", "DIAMOND":"D", "PLATINUM":"P", "GOLD":"G", "SILVER":"S", "BRONZE":"B"}

        ##FRAME WILL BE 1920x1080
        backFrame = Frame(master,bg="black")
        backFrame.pack()

        ##Feed Image raw data to PIL to change it to something useful
        imagePIL = Image.open("wallpaperDARK.jpg")
        image = ImageTk.PhotoImage(imagePIL)
        
        ##Actually place the image
        label = Label(backFrame,image=image)
        label.image= image
        label.pack()

        inputFrame = Frame(backFrame,bg="black",width=300,height=150)
        inputFrame.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.sumName = StringVar()
        self.sumName.set("Summoner Name...")
        inputSumm = Entry(inputFrame, textvariable=self.sumName)

        self.region = StringVar(master)
        self.region.set("na")
        inputRegion = OptionMenu(inputFrame,self.region,"br","eune","euw","kr","lan","las","na","oce","ru","tr")

        submitButton = Button(inputFrame,text="Search Game",command=self.search)
        
        inputSumm.pack(side=TOP,fill=X,padx=5,pady=5)
        inputRegion.pack(side=TOP,fill=X,padx=5,pady=5)
        submitButton.pack(side=TOP,fill=X,padx=5,pady=5)

        currentGameFrame = Frame(backFrame,bg="black",width=900,height=650)
        currentGameFrame.place(relx=0.3, rely=0.57, anchor=CENTER)

        currentGameFrame.pack_propagate(0)
        
        currentGameFrameTop = Frame(currentGameFrame,bg="blue",height=325,width = 900)
        currentGameFrameBot = Frame(currentGameFrame,bg="red",height=325,width = 900)

        currentGameFrameTop.grid_propagate(0)
        currentGameFrameBot.grid_propagate(0)
        
        currentGameFrameTop.pack(side=TOP)
        currentGameFrameBot.pack(side=TOP)

        currentGameFramePlayers1 = [Frame(currentGameFrameTop,bg="black",height=320,width = 176) for i in range(5)]
        currentGameFramePlayers2 = [Frame(currentGameFrameBot,bg="black",height=320,width = 176) for i in range(5)]
        currentGameFramePlayers = currentGameFramePlayers1 + currentGameFramePlayers2

        for i in range(10):
            currentGameFramePlayers[i].pack_propagate(0)
            currentGameFramePlayers[i].grid_propagate(0)

        self.imagesLabelsChampion=[Label(currentGameFramePlayers[i],bg="black") for i in range(10)]

        statBox=[Frame(currentGameFramePlayers[i],bg="black",height=125,width = 176) for i in range(10)]

        wlLabel =[Label(statBox[i],bg="black",fg="white",text = "W/L:", anchor=W,justify=LEFT) for i in range(10)]
        killsLabel =[Label(statBox[i],bg="black",fg="white",text = "Kills:", anchor=W,justify=LEFT) for i in range(10)]
        deathsLabel =[Label(statBox[i],bg="black",fg="white",text = "Deaths:", anchor=W,justify=LEFT) for i in range(10)]
        assistsLabel =[Label(statBox[i],bg="black",fg="white",text = "Assists:", anchor=W,justify=LEFT) for i in range(10)]
        csLabel =[Label(statBox[i],bg="black",fg="white",text = "CS:", anchor=W,justify=LEFT) for i in range(10)]
        goldLabel =[Label(statBox[i],bg="black",fg="white",text = "Gold:", anchor=W,justify=LEFT) for i in range(10)]

        self.rankImLabel = [Label(statBox[i],bg="black") for i in range(10)]

        self.wlVar = [StringVar(master) for i in range(10)]
        self.killsVar = [StringVar(master) for i in range(10)]
        self.deathsVar = [StringVar(master) for i in range(10)]
        self.assistsVar = [StringVar(master) for i in range(10)]
        self.csVar = [StringVar(master) for i in range(10)]
        self.goldVar = [StringVar(master) for i in range(10)]

        self.rankTextVar = [StringVar(master) for i in range(10)]

        for i in range(10):
            self.wlVar[i].set("0/0")
            self.killsVar[i].set("-")
            self.deathsVar[i].set("-")
            self.assistsVar[i].set("-")
            self.csVar[i].set("-")
            self.goldVar[i].set("-")
            self.rankTextVar[i].set("")
            imagePIL = Image.open("tier_small/unknown.png")
            image = ImageTk.PhotoImage(imagePIL)
            self.rankImLabel[i].configure(image = image)
            self.rankImLabel[i].image = image

        wlValLabel =[Label(statBox[i],bg="black",fg="white",textvariable=self.wlVar[i], anchor=W,justify=LEFT) for i in range(10)]
        killsValLabel =[Label(statBox[i],bg="black",fg="white",textvariable=self.killsVar[i], anchor=W,justify=LEFT) for i in range(10)]
        deathsValLabel =[Label(statBox[i],bg="black",fg="white",textvariable=self.deathsVar[i], anchor=W,justify=LEFT) for i in range(10)]
        assistsValLabel =[Label(statBox[i],bg="black",fg="white",textvariable=self.assistsVar[i], anchor=W,justify=LEFT) for i in range(10)]
        csValLabel =[Label(statBox[i],bg="black",fg="white",textvariable=self.csVar[i], anchor=W,justify=LEFT) for i in range(10)]
        goldValLabel =[Label(statBox[i],bg="black",fg="white",textvariable=self.goldVar[i], anchor=W,justify=LEFT) for i in range(10)]

        rankTextLabel =[Label(statBox[i],bg="black",fg="white",textvariable=self.rankTextVar[i]) for i in range(10)]
        

        for i in range(10):
            currentGameFramePlayers[i].grid(row=0,column=i,padx=2,pady=2)
            self.imagesLabelsChampion[i].pack(side=TOP,fill=BOTH)
            statBox[i].pack(side=BOTTOM)

            wlLabel[i].grid(row=0,column=0,sticky=W)
            killsLabel[i].grid(row=1,column=0,sticky=W)
            deathsLabel[i].grid(row=2,column=0,sticky=W)
            assistsLabel[i].grid(row=3,column=0,sticky=W)
            csLabel[i].grid(row=4,column=0,sticky=W)
            goldLabel[i].grid(row=5,column=0,sticky=W)
            wlValLabel[i].grid(row=0,column=1,sticky=W)
            killsValLabel[i].grid(row=1,column=1,sticky=W)
            deathsValLabel[i].grid(row=2,column=1,sticky=W)
            assistsValLabel[i].grid(row=3,column=1,sticky=W)
            csValLabel[i].grid(row=4,column=1,sticky=W)
            goldValLabel[i].grid(row=5,column=1,sticky=W)
            self.rankImLabel[i].grid(row=0,column=2,rowspan=3,columnspan=2,sticky=E)
            rankTextLabel[i].grid(row=3,column=2,columnspan=2)
            
        self.images = []
        self.rankedStats = []
        self.leagues = []

            
    def search(self):
        ##This is what the button does
        self.images = []
        self.rankedStats = []
        self.leagues = []
        try:
            name = self.sumName.get()
            name = name.lower()
            name = list(name)
            while ' ' in name:
                name.remove(' ')
            name = "".join(name)
            playerInfo = self.api.getSummonerByName(self.region.get(),name)
            currentMatch = self.api.getCurrentGame(self.plaformsId[self.region.get()],playerInfo.id)
            for i in range(10):
                self.setImages(i,self.api.getChampion(self.region.get(),currentMatch.participants[i].championId).key)
                try:
                    self.rankedStats.append(self.api.getRankedStats(self.region.get(),currentMatch.participants[i].summonerId))
                    index = -1
                    for j in range(len(self.rankedStats[-1].champions)):
                        if self.rankedStats[-1].champions[j].id == currentMatch.participants[i].championId:
                            index = j
                            break
                    if index != -1:
                        stats = self.rankedStats[-1].champions[index].stats
                        if stats.totalSessionsPlayed ==0:
                            continue
                        winrate = str(100.0*stats.totalSessionsWon/stats.totalSessionsPlayed)
                        winrate = winrate[:winrate.index('.')+2]
                        killAve = str(1.0*stats.totalChampionKills/stats.totalSessionsPlayed)
                        killAve = killAve[:killAve.index('.')+2]
                        deathAve = str(1.0*stats.totalDeathsPerSession/stats.totalSessionsPlayed)
                        deathAve = deathAve[:deathAve.index('.')+2]
                        assistsAve = str(1.0*stats.totalAssists/stats.totalSessionsPlayed)
                        assistsAve = assistsAve[:assistsAve.index('.')+2]
                        csAve = str(1.0*stats.totalMinionKills/stats.totalSessionsPlayed)
                        csAve = csAve[:csAve.index('.')+2]
                        goldAve = str(1.0*stats.totalGoldEarned/stats.totalSessionsPlayed)
                        goldAve = goldAve[:goldAve.index('.')+2]
                        
                        self.wlVar[i].set(str(stats.totalSessionsWon)+"/"+str(stats.totalSessionsLost) + " ("+winrate+")" )
                        self.killsVar[i].set(killAve)
                        self.deathsVar[i].set(deathAve)
                        self.assistsVar[i].set(assistsAve)
                        self.csVar[i].set(csAve)
                        self.goldVar[i].set(goldAve)
                except urllib.error.HTTPError:
                    self.wlVar[i].set("0/0")
                    self.killsVar[i].set("-")
                    self.deathsVar[i].set("-")
                    self.assistsVar[i].set("-")
                    self.csVar[i].set("-")
                    self.goldVar[i].set("-")
                    self.rankTextVar[i].set("")

                try:
                    self.leagues.append(self.api.getLeague(self.region.get(),currentMatch.participants[i].summonerId))
                    index = -1
                    for j in range(len(self.leagues[-1].leagues)):
                        if self.leagues[-1].leagues[j].queue == "RANKED_SOLO_5x5":
                            index = j
                            break
                    if index == -1:
                        imagePIL = Image.open("tier_small/unknown.png")
                        image = ImageTk.PhotoImage(imagePIL)
                        self.rankImLabel[i].configure(image = image)
                        self.rankImLabel[i].image = image
                        continue
                    league = self.leagues[-1].leagues[index]
                    tier = league.tier
                    division = ""
                    for j in range(len(league.entries)):
                        if int(league.entries[j].playerOrTeamId) == int(currentMatch.participants[i].summonerId):
                            division = league.entries[j].division
                            break
                    self.rankTextVar[i].set(self.tiers[tier]+division)
                    imagePIL = Image.open("tier_small/" + tier+"_"+ division+ ".png")
                    image = ImageTk.PhotoImage(imagePIL)
                    self.images.append(image)
                    self.rankImLabel[i].configure(image = image)
                    self.rankImLabel[i].image = self.images[-1]
                except urllib.error.HTTPError as e:
                    imagePIL = Image.open("tier_small/unknown.png")
                    image = ImageTk.PhotoImage(imagePIL)
                    self.rankImLabel[i].configure(image = image)
                    self.rankImLabel[i].image = image
        except urllib.error.HTTPError as e:
            if e.code ==403:
                self.sumName.set("Forbiden")
            if e.code ==429:
                self.sumName.set("Rate limit exceeded")
            if e.code ==404:
                self.sumName.set("invalid name")
            if e.code == 500:
                self.sumName.set("Server error")
            if e.code == 503:
                self.sumName.set("Service unavailable")
            if e.code == 400:
                self.sumName.set("Bad Request")
            if e.code == 401:
                self.sumName.set("Unauthorized")
            for i in range(10):
                imagePIL = Image.open("tier_small/unknown.png")
                image = ImageTk.PhotoImage(imagePIL)
                self.rankImLabel[i].configure(image = image)
                self.rankImLabel[i].image = image
                self.wlVar[i].set("0/0")
                self.killsVar[i].set("-")
                self.deathsVar[i].set("-")
                self.assistsVar[i].set("-")
                self.csVar[i].set("-")
                self.goldVar[i].set("-")
                self.rankTextVar[i].set("")
                self.imagesLabelsChampion[i].configure(image="")

        
    def setImages(self, position, name):
        label = self.imagesLabelsChampion[position]
        imagePIL = Image.open("ChampPics/" + name + ".jpg")
        image = ImageTk.PhotoImage(imagePIL)
        self.images.append(image)
        label.configure(image = image)
        label.image = self.images[-1]



root = Tk()


test = GUIwindow(root,"5401f52d-7f01-46eb-80c6-a49509a4d9bb")
root.mainloop()
