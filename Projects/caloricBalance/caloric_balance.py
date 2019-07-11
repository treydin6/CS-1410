class CaloricBalance:
    
    def __init__(self, gender, age, height, weight):
        self.weight = weight
        self.balance = -self.getBMR(gender, age, height, weight)

    def getBMR(self, gender, age, height, weight):
        if gender == 'm':
            return  66 + (12.7 * height) + (6.23 * weight) - (6.8 * age)
        elif gender == 'f':
            return 655 + (4.7 * height) + (4.35 * weight) - (4.7 * age)
        else:
            return 0.0

    def getBalance(self):
        return self.balance

    ## Caloric Burn Per Pound Per Minute
    def recordActivity(self, CBPPPM, minutes):
        CBPM = CBPPPM * self.weight       # Calories buurned per minute
        CB = CBPM * minutes               # Caloric Balance
        self.balance -= CB

    def eatFood(self, calories):
        self.balance += calories
