# Question 1

class Food(object):
    def _init_(self, name, nutrition_value, good_until):
        self.name = name
        self.nutrition_value = nutrition_value
        self.good_until = good_until
        
    def sit_there(self, time):
        self.good_until += time
    
    def eat(self):
        if self.nutrition_value > 0:
            return self.nutrition_value
        else:
            return 0

class AgedFood(Food):
    def _init_(self, good_after):
        self.good_after = good_after
        
    def sniff(self):
        if self.