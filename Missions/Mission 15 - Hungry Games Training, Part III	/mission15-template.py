#
# CS1010X --- Programming Methodology
#
# Mission 15 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from engine import *
import simulation
import random

# Rename XX_AI to YourName_AI
class XX_AI(Tribute):
    def next_action(self):
        # Next action should return a tuple of what your next action should
        # be. For the full list of tuple that your AI can return, refer to
        # the pdf file
        
        # ENVIRONMENT SCANNER
        
        objects = self.objects_around() # return all objects present in area
        weapons_around = [] # list of weapons present lying around area
        enemy_count = 0 # number of hostile creatures in area (Tribute or WildAnimal)
        
        # MOVEMENTS
        
        def move():
            exits = self.get_exits()
            if exits:
                index = random.randint(0, len(exits)-1)
                direction = exits[index]
                return ("GO", direction)
        
        if len(objects) == 0: 
            return move() # move elsewhere if empty surrounding
        else: # if objects in area:
            for i in objects:
                if isinstance(i, Tribute) or isinstance(i, WildAnimal): # if object is enemy
                    enemy_count += 1
                if isinstance(i, Weapon) or isinstance(i, RangedWeapon): # if object is weapon
                    weapons_around.append(i)
                
        weapons_around.sort(key=lambda x: x.max_damage(), reverse=True) # sorting weapons around area by max damage
        weapons_carried = list(self.get_weapons()) 
        weapons_carried.sort(key=lambda x: x.max_damage(), reverse=True) # sorting weapons in inventory by max damage
        
        # WEAPON SELECTION
        
        if len(weapons_carried) == 0: # if no weapons in inventory:
            if len(weapons_around) > 0:
                return ("TAKE", weapons_around[0]) # take weapon with maximum damage from area
        else:           
            if enemy_count == 0 and len(weapons_around) > 0: # if no enemies: collect all weapons in area
                return ("TAKE", weapons_around[0]) 
            
            chosen_index = 0
            chosen_weapon = weapons_carried[chosen_index] # selecting the most powerful weapon in inventory
            
            """
            if top weapon is RangedWeapon:
            if ranged weapon has ammo, break the loop, move on. else:
            if have ammo in inventory, load weapon with ammo from inventory
            if no ammo in inventory, search in area. if area has, take and load
            else, increment chosen_index: select next most powerful weapon, repeat loop
            if top weapon is not ranged, break loop, move on
            """
            
            while True:
                if isinstance(chosen_weapon, RangedWeapon):
                    if chosen_weapon.shots_left() == 0: # if no ammo                      
                        for i in self.get_inventory():
                            if isinstance(i, Ammo) and i.weapon_type() == chosen_weapon.get_name():
                                return ("LOAD", chosen_weapon, i) # if ammo type matches weapon, load weapon
                        for i in objects:
                            if isinstance(i, Ammo) and i.weapon_type() == chosen_weapon.get_name():
                                return ("TAKE", i) # if ammo type matches weapon, take it from area
                        chosen_index += 1 # if no ammo in inventory nor area:
                        if chosen_index == len(weapons_carried):
                            return move() # if no ammo for all weapons in inventory, search in another area
                        else:
                            chosen_weapon = weapons_carried[chosen_index] # choose next most powerful weapon
                    else:
                        break # if ranged weapon has ammo: break
                else:
                    break # if top weapon is not ranged: break
                
        # MISCELLANEOUS
        
        for i in objects:
            if self.get_hunger() >= 80: # if hunger >= 80:
                food = list(self.get_food()) # list of food in inventory
                food.sort(key=lambda x: x.get_food_value(), reverse=True) # sorting food by food value
                if len(food) > 0:
                    return ("EAT", food[0]) # if have food, eat most potent food
                else:
                    for j in objects:
                        # if no food AND no enemies around, search area for food and take if any
                        if (isinstance(i, Food) or isinstance(i, Medicine)) and enemy_count == 0:
                            return ("TAKE", i)
                    return move() # if enemies around or if no food, move elsewhere
            elif self.get_health() <= 20: # if health <= 20:
                meds = list(self.get_medicine()) # list of meds in inventory
                meds.sort(key=lambda x: x.get_medicine_value(), reverse=True) # sorting meds by potency
                if len(meds) > 0:
                    return ("EAT", meds[0]) # if have meds, eat most potent meds
                else:
                    for j in objects:
                        # if no meds nad no enemies around, search area for meds and take if any
                        if (isinstance(i, Food) or isinstance(i, Medicine)) and enemy_count == 0:
                            return ("TAKE", i)
                    return move() # if enemies around or no meds, move elsewhere
            elif (isinstance(i, Animal) or isinstance(i, Tribute)) and len(self.get_weapons()) > 0:
                return ("ATTACK", i, chosen_weapon) # if have weapon and hunger and health is OK: attack
            elif (isinstance(i, Animal) or isinstance(i, Tribute)) and len(self.get_weapons()) == 0:
                return move() # if no weapon in inventory AND no weapon in area: move
            elif isinstance(i, Food) or isinstance(i, Medicine) or isinstance(i, Ammo):
                return ("TAKE", i) # attacking takes precdence over collecting food/meds/ammo


# NOTE: DO NOT remove the 2 lines of code below.
#
# In particular, you will need to modify the `your_AI = XX_AI` line so that
# `XX_AI` is the name of your AI class.
# For instance, if your AI class is called `MyPrecious_AI`, then you have to
# modify that line to:
#
#     your_AI = MyPrecious_AI
#
# Failure to do so will result in the following exception on Coursemology when
# you run the test cases:
#
#     Traceback (most recent call last):
#       in <module>
#     NameError: name 'your_AI' is not defined
#
# You have been warned!
time_limit = 50 # Modify if your AI needs more than 50 moves for task 2
your_AI = XX_AI # Modify if you changed the name of the AI class

##################
# Simulation Code
##################
##########
# Task 1 #
##########
# Goal:
# 1. Your AI should be able to pick up a Weapon / RangedWeapon
# 2. Your AI should be able to kill chicken
# 3. Your AI should be able to pick up chicken_meat after killing chicken

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
#simulation.task1(XX_AI("XX AI", 100), gui=True)

##########
# Task 2 #
##########
## 1. Your AI should be able to pick up a Weapon / RangedWeapon
## 2. Your AI should be able to move around and explore
## 3. Your AI should be able to find harmless Tribute and kill him

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI

time_limit = 20    # You may change the time limit if your AI is taking too long
#simulation.task2(XX_AI("XX AI", 100), time_limit, gui=True)

#################
# Optional Task
#################
## You can create your own map and see how your AI behaves!

# Define the parameters of the map
def config():
    ## The game should have a 3x3 map
    game_map = GameMap(3)

    ## You can change the numbers to create different kinds of maps for
    ## the optional task.
    game_config = GameConfig()
    game_config.set_item_count(Weapon, 3)
    game_config.set_item_count(Animal, 10)
    game_config.set_item_count(RangedWeapon, 5)
    game_config.set_item_count(Food, 5)
    game_config.set_item_count(Medicine, 5)

    game = GameEngine(game_map, game_config)

    # Add some dummy tributes
    ryan = Tribute("Ryan", 100)
    waihon = Tribute("Wai Hon", 100)
    soedar = Tribute("Soedar", 100)

    game.add_tribute(ryan)
    game.add_tribute(waihon)
    game.add_tribute(soedar)

    # Yes, your AI can fight with himself
    #ai_clone = XX_AI("AI Clone", 100)
    #game.add_tribute(ai_clone)

    return game

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
#simulation.optional_task(XX_AI("XX AI", 100), config, gui=False)