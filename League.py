

class LeagueEntry:

    def __init__(self,data):
        self.division = data['division']
        self.isFreshBlood = data['isFreshBlood']
        self.isHotStreak = data['isHotStreak']
        self.isInactive = data['isInactive']
        self.isVeteran = data['isVeteran']
        self.leaguePoints = data['leaguePoints']
        self.losses = data['losses']
        self.playerOrTeamId = data['playerOrTeamId']
        self.playerOrTeamName = data['playerOrTeamName']
        self.wins = data['wins']


class League:

    def __init__(self,data):
        self.entries = [LeagueEntry(data['entries'][i]) for i in range(len(data['entries']))]
        self.name = data['name']
        self.participantId = data['participantId']
        self.queue = data['queue']
        self.tier = data['tier']


class LeagueList:

    def __init__(self,data):
        self.leagues = [League(data[i]) for i in range(len(data))]
