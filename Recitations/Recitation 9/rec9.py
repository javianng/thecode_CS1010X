# Question 1

from xxlimited import foo


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
        return self.age > self.good_after
        
    def eat(self): # ??????????????????????????????
        if self.sniff():
            return super().eat(self.age)
        else:
            return 0
        
# Question 3

class VendingMachine(object):
    def __init__(self, name, nutrition, good_until):
        self.name = name
        self.nutrition = nutrition
        self.good_until = good_until
        self.age = 0
        
    def sit_there(self, time):
        self.age += time/2
        
    def sell_food(self):
        food = Food(self.name, self.nutrition, self.good_until)
        food.age = self.age
        return food
    
# Question 4

def mapn(function, lsts):
    return tuple(map(function, *lsts)) # the * allows you to take in more than one lst

# Question 5

class VendingMachine(object):
    def __init__(self, type_food, name, nutrition, good_until, *good_after):
        self.name = name
        self.nutrition = nutrition
        self.good_until = good_until
        self.age = 0
        self.type_food = type_food
        
    def sit_there(self, time):
        self.age += time/2
        
    def sell_food(self):
        if ...
        food = self.type_food(self.name, self.nutrition, self.good_until)
        food.age = self.age
        return food
    
    def sell_agedFood(self):
        ...