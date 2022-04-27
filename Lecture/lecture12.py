##############
# Question 1 #
##############
class Mammal(object):
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def say(self):
        return "What does the " + self.name + " say"

# print(Mammal("Dog").get_name())
# print(Mammal("Dog").say())

##############
# Question 2 #
##############

# You DO NOT NEED TO DEFINE Mammal class here!
class Dog(Mammal):
    def __init__(self):
        self.name = 'Dog'
        super().__init__('Dog')

# Cat definition should go here

class Cat(Mammal):
    def __init__(self):
        self.name = 'Cat'
        super().__init__('Cat')
        
# Fox definition should go here

class Fox(Mammal):
    def __init__(self):
        self.name = 'Fox'
        super().__init__('Fox')

# print(Dog().get_name())

##############
# Question 3 #
##############

# You DO NOT NEED TO DEFINE Mammal class here!

# Implement additional methods to your Dog, Cat and Fox subclasses to modify what they say.

