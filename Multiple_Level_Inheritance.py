class Family:
    def __init__(self, address) -> None:
        self.address = address

class School(Family):
    def __init__(self, address, name, location, level) -> None:
        super().__init__(address)
        self.name = name
        self.location = location
        self.level = level

class Sports(School):
    def __init__(self, address, name, location, level, sport_name, team_name) -> None:
        super().__init__(address, name, location, level)
        self.sport_name = sport_name
        self.team_name = team_name      

class Students(Family, School, Sports):
    def __init__(self, address, name, location, level, sport_name, team_name, student_name, grade) -> None:
        Family.__init__(self, address)
        School.__init__(self, address, name, location, level)
        Sports.__init__(self, address, name, location, level, sport_name, team_name)
        self.student_name = student_name
        self.grade = grade                      


        
       
     