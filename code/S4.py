class Team:
    def __init__(self, mate1, mate2):
        self.__mate1=mate1
        self.__mate2=mate2
    
    def members(self):
        print (f"Red Bull members is {self.__mate1} and {self.__mate2}")

rb_team=Team('Verstappen', 'Perez')
rb_team.members()