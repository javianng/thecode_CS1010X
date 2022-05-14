# Question 1

class Thing(object):
    def __init__(self, name):
        self.name = name
        self.owner = None

    def is_owned(self):
        return self.owner is not None
    
    def get_owner(self):
        return self.owner
    
stone = Thing('stone')

# Task 2: Extend Thing

class Thing(object):
    def __init__(self, name):
        self.name = name
        self.owner = None
        self.place = None

    def is_owned(self):
        return self.owner is not None
    
    def get_owner(self):
        return self.owner
    
    def get_name(self):
        return self.name
    
    def get_place(self):
        return self.place

# Task 3: Inheritance from MobileObject

# class Thing(MobileObject):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#         self.owner = None
#         self.place = None

#     def is_owned(self):
#         return self.owner is not None
    
#     def get_owner(self):
#         return self.owner

from hungry_games import *
burger1 = Thing("burger")
burger2 = Thing("burger")

# print(burger1 == burger2)