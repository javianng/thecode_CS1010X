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

class Dog(Mammal):
    def __init__(self):
        self.name = 'Dog'
        super().__init__('Dog')
    def say(self):
        return "Woof"
        
# Cat definition should go here

class Cat(Mammal):
    def __init__(self):
        self.name = 'Cat'
        super().__init__('Cat')
    def say(self):
        return "Meow"
        
# Fox definition should go here

class Fox(Mammal):
    def __init__(self):
        self.name = 'Fox'
        super().__init__('Fox')
    def say(self):
        return "Ring-ding-ding-ding-dingeringeding"
        
# print(Dog().say())
# print(Mammal("Dog").say())

######################
# Question 4: Artist #
######################

class Artist(object):
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
    def get_name(self):
        return self.name
        
    def get_dob(self):
        return self.dob
        
# Used for public test cases.
# You DO NOT have to include this in your submission.
jt = Artist("Justin Timberlake", (1981, 1, 31))

# print(jt.get_name())
# print(jt.get_dob())
# print(Artist("JC Chasez", (1976, 8, 8)).get_name())

##########################
# Question 5: Artist Age #
##########################

def get_date_today():
    return (2013, 10, 30)

def leap_year_identifier(year):
    '''if year = leap year, return True, otherwise False'''
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 ==0) and (year % 100 != 0):
        return True
    else:
        return False
    
class Artist(object):
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
    def age(self):
        list_dob = list(self.dob)
        # for people with birthday on 29th of feb
        if list_dob[1] == 2 and list_dob[2] == 29:
            # if year is not leap year
            if leap_year_identifier(get_date_today()[0]) == True:
                list_dob[1], list_dob[2] = 3, 1
        
        # print(list_dob)
        
        number = get_date_today()[0] - list_dob[0]
        
        if list_dob[1] > get_date_today()[1]:
            return number - 1
        elif list_dob[1] == get_date_today()[1]:
            if list_dob[2] >= get_date_today()[2]:
                return number - 1
            else:
                return number
        else:
            return number
        

# Used for public test cases.
# You DO NOT have to include this in your submission
# jt = Artist("Justin Timberlake", (1981, 1, 31))

# print(jt.age())
print(Artist("Hayley Williams", (1980, 2, 29)).age())