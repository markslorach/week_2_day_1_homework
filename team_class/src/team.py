class Team:
    points = 0
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player):
        return player in self.players
    
   # extensions
   

