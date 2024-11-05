class Team:
    def __init__(self, mate1, mate2):
        self.mate1=mate1
        self.mate2=mate2
    
    def members(self):
        print (f"Red Bull members is {self.mate1} and {self.mate2}")

rb_team=Team('Verstappen', 'Perez')
rb_team.members()

class Leader(Team):
    def __init__(self, mate1, mate2):
        super().__init__(mate1, mate2)
    def leader(self):
        print(f'McLaren team leader is {self.mate1}')

team_lead=Leader('Norris', 'Piastri')
team_lead.leader()