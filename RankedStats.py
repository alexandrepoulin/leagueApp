

class AggregatedStats:

    def __init__(self,data):
        self.totalDeathsPerSession = data['totalDeathsPerSession']
        self.totalSessionsPlayed = data['totalSessionsPlayed']
        self.totalDamageTaken = data['totalDamageTaken']
        self.totalQuadraKills = data['totalQuadraKills']
        self.totalTripleKills = data['totalTripleKills']
        self.totalMinionKills = data['totalMinionKills']
        self.maxChampionsKilled = data['maxChampionsKilled']
        self.totalDoubleKills = data['totalDoubleKills']
        self.totalPhysicalDamageDealt = data['totalPhysicalDamageDealt']
        self.totalChampionKills = data['totalChampionKills']
        self.totalAssists = data['totalAssists']
        self.mostChampionKillsPerSession = data['mostChampionKillsPerSession']
        self.totalDamageDealt = data['totalDamageDealt']
        self.totalFirstBlood = data['totalFirstBlood']
        self.totalSessionsLost = data['totalSessionsLost']
        self.totalSessionsWon = data['totalSessionsWon']
        self.totalMagicDamageDealt = data['totalMagicDamageDealt']
        self.totalGoldEarned = data['totalGoldEarned']
        self.totalPentaKills = data['totalPentaKills']
        self.totalTurretsKilled = data['totalTurretsKilled']
        self.mostSpellsCast = data['mostSpellsCast']
        self.maxNumDeaths = data['maxNumDeaths']
        self.totalUnrealKills = data['totalUnrealKills']


class ChampionStats:

    def __init__(self,data):
        self.id = data['id']
        self.stats = AggregatedStats(data['stats'])


class RankedStats:

    def __init__(self,data):
        self.champions = [ChampionStats(data['champions'][i]) for i in range(len(data['champions']))]
        self.modifyDate = data['modifyDate']
        self.summonerId = data['summonerId']
