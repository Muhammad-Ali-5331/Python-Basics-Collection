class Warrior:
    RANKS = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master",
             "Greatest"]


    def __init__(self):
        self.level = 1
        self.experience = 100
        self.achievements = []
        self.rank = ""
        self.updateRank()


    def checkExperience(self):
        return self.experience <=10**4


    def updateExperience(self,val):
        if self.checkExperience() and self.experience+val<=10**4:
            self.experience+=val
            self.updateRank()

    def updateLevel(self):
        if self.checkExperience():
            self.level = self.experience//100


    def updateRank(self):
        self.updateLevel()
        self.rank = Warrior.RANKS[self.level//10]


    def battle(self,enemyLevel):
        if 1<=enemyLevel<=100:
            res = ""
            if enemyLevel == self.level:
                experience = 10
                res = "A good fight"
            elif enemyLevel == self.level-1:
                experience = 5
                res = "A good fight"
            elif enemyLevel<=self.level-2:
                experience = 0
                res = "Easy fight"
            elif self.level == enemyLevel-5 and Warrior.RANKS.index(self.rank) == Warrior.RANKS.index(enemyLevel//100)-1:
                return "You've been defeated"
            else:
                diff = enemyLevel-self.level
                experience = 20 * diff * diff
                res = "An intense fight"
            self.updateExperience(experience)
            return res
        else:
            return "Invalid level"


    def training(self,items):
        if items[2]<=self.level:
            self.achievements.append(items[0])
            self.updateExperience(items[1])
            return items[0]
        else:
            return "Not strong enough"