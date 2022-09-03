class User:
    def __init__(self, major, stuid, name):
        self.major = major
        self.id = stuid
        self.name = name
        self.score = 10
        
    def add_score(self, score):
        self.score += score
    
    def sub_score(self, score):
        self.score -= score
        
    def if_minus_set_zero(self):
        if self.score < 0:
            self.score = 0