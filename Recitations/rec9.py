# Question 1

class Food(object):
    def __init__(self, name, nutrition, good_until):
        self.name = name
        self.nutrition = nutrition
        self.good_until = good_until
        self.age = 0
        
    def sit_there(self, time):
        self.age += time
    
    def eat(self):
        if self.age <= self.good_until:
            return self.nutrition
        else:
            return 0

# Question 2

class AgedFood(Food):
    def __init__(self, name, nutrition, good_until, good_after):
        super().__init__(name, nutrition, good_until)
        self.good_after = good_after
        
    def sniff(self):
        if self.age > self.good_after:
            return True
        else:
            return False
        
    def eat(self)