

class Champion:

    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.name = data['name']
        self.key = data['key']

class ChampionList:

    def __init__(self,data):
        self.data = [Champion(data['data'][i]) for i in data['data'].keys()]
        self.type = data['type']
        self.version = data['version']

