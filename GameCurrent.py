
class Mastery:

    def __init__(self,data):
        self.masteryId = data['masteryId']
        self.rank = data['rank']

class Rune:

    def __init__(self,data):
        self.count = data['count']
        self.runeId = data['runeId']

class BannedChampion:

    def __init__(self,data):
        self.championId = data['championId']
        self.pickTurn = data['pickTurn']
        self.teamId = data['teamId']

class Observer:

    def __init__(self,data):
        self.encryptionKey = data['encryptionKey']

class Participant:

    def __init__(self,data):
        self.bot = data['bot']
        self.championId = data['championId']
        self.masteries = [Mastery(data['masteries'][i]) for i in range(len(data['masteries']))]
        self.profileIconId = data['profileIconId']
        self.runes = [Rune(data['runes'][i]) for i in range(len(data['runes']))]
        self.spell1Id = data['spell1Id']
        self.spell2Id = data['spell2Id']
        self.summonerId = data['summonerId']
        self.summonerName = data['summonerName']
        self.teamId = data['teamId']

class CurrentGame:

    def __init__(self,data):
        self.bannedChampions = [BannedChampion(data['bannedChampions'][i]) for i in range(len(data['bannedChampions']))]
        self.gameId = data['gameId']
        self.gameLength = data['gameLength']
        self.gameMode = data['gameMode']
        self.gameQueueConfigId = data['gameQueueConfigId']
        self.gameStartTime = data['gameStartTime']
        self.gameType = data['gameType']
        self.mapId = data['mapId']
        self.observers = Observer(data['observers'])
        self.participants = [Participant(data['participants'][i]) for i in range(len(data['participants']))]
        self.platformId = data['platformId']

   
