
from GameStats import *

class MasteryHistory:

    def __init__(self,data):
        self.masteryId = data['masteryId']
        self.rank = data['rank']

class RuneHistory:

    def __init__(self,data):
        self.rank = data['rank']
        self.runeId = data['runeId']

class ParticipantTimelineData:

    def __init__(self,data):
        self.zeroToTen = data['zeroToTen']
        self.tenToTwenty = 0
        self.thirtyToEnd = 0
        self.twentyToThirty = 0
        keys = data.keys()
        if 'tenToTwenty' in keys:
            self.tenToTwenty = data['tenToTwenty']
        if 'twentyToThirty' in keys:
            self.twentyToThirty = data['twentyToThirty']
        if 'thirtyToEnd' in keys:
            self.thirtyToEnd = data['thirtyToEnd']
        

class ParticipantTimeline:

    def __init__(self,data):
        self.xpPerMinDeltas = ParticipantTimelineData(data['xpPerMinDeltas'])
        self.goldPerMinDeltas = ParticipantTimelineData(data['goldPerMinDeltas'])
        self.damageTakenPerMinDeltas = ParticipantTimelineData(data['damageTakenPerMinDeltas'])
        self.role = data['role']
        self.creepsPerMinDeltas = ParticipantTimelineData(data['creepsPerMinDeltas'])
        self.csDiffPerMinDeltas = ParticipantTimelineData(data['csDiffPerMinDeltas'])
        self.xpDiffPerMinDeltas = ParticipantTimelineData(data['xpDiffPerMinDeltas'])
        self.damageTakenDiffPerMinDeltas = ParticipantTimelineData(data['damageTakenDiffPerMinDeltas'])
        self.lane = data['lane']

class Participant:

    def __init__(self,data):
        self.championId = data['championId']
        self.highestAchievedSeasonTier = data['highestAchievedSeasonTier']
        self.masteries = [MasteryHistory(data['masteries'][i]) for i in range(len(data['masteries']))]
        self.participantId = data['participantId']
        self.runes = [RuneHistory(data['runes'][i]) for i in range(len(data['runes']))]
        self.spell1Id = data['spell1Id']
        self.spell2Id = data['spell2Id']
        self.stats = ParticipantStats(data['stats'])
        self.teamId = data['teamId']
        self.timeline = ParticipantTimeline(data['timeline'])

class Player:

    def __init__(self,data):
        self.matchHistoryUri = data['matchHistoryUri']
        self.profileIcon = data['profileIcon']
        self.summonerId = data['summonerId']
        self.summonerName = data['summonerName']

class ParticipantIdentity:

    def __init__(self,data):
        self.participantId = data['participantId']
        self.player = Player(data['player'])

class MatchHistory:

    def __init__(self,data):
        self.mapId = data['mapId']
        self.matchCreation = data['matchCreation']
        self.matchDuration = data['matchDuration']
        self.matchId = data['matchId']
        self.matchMode = data['matchMode']
        self.matchType = data['matchType']
        self.matchVersion = data['matchVersion']
        self.participantIdentities = [ParticipantIdentity(data['participantIdentities'][i]) for i in range(len(data['participantIdentities']))]
        self.participants = [Participant(data['participants'][i]) for i in range(len(data['participants']))]
        self.platformId = data['platformId']
        self.queueType = data['queueType']
        self.region = data['region']
        self.season = data['season']


class History:

    def __init__(self,data):
        self.matches = [MatchHistory(data['matches'][i]) for i in range(len(data['matches']))]
     
