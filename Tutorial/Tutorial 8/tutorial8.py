#######################
# Question 1: Widget! #
#######################

def make_widget():
    stuff = ["empty", "empty", 0]
    def oplookup(msg, *args):                         # *arg -> arbitrary number of arguements
        if msg == "insert":
            place = stuff[2]
            stuff[place] = args[0]
            stuff[2] = (place + 1) % 2
        elif msg == "retrieve":
            return stuff[stuff[2]]
        else:
            raise Exception("widget doesn’t " + msg)
    return oplookup

widget = make_widget()

print(widget)
widget('insert', 1)
print(widget('retrieve'))
widget('insert', 2)
print(widget('retrieve'))
widget('insert', 3)
print(widget('retrieve'))

###########################
# Question 2: Accumulator #
###########################

def make_accumulator():
    acc = 0
    def helper(x):
        nonlocal acc         # acc will now be linked to the acc outside of this helper function
        acc += x
        return acc
    return helper

def make_accumulator():
    acc = [0]
    def helper(x):
        acc[0] += x
        return acc[0]
    return helper

# acc = 1
# def make_accumulator():
#     acc = 0
#     def helper(x):
#         nonlocal acc  # this will result in the acc = 0 being used
#         acc += x
#         return acc
#     return helper

# acc = 1
# def make_accumulator():
#     acc = 0
#     def helper(x):
#         global acc  # this will result in the acc = 1 being used
#         acc += x
#         return acc
#     return helper

# acc = 1
# def make_accumulator():
#     acc = 2
#     def f():
#         acc = 3
#         def helper(x):
#             global acc  # this will result in the acc = 3 being used
#             acc += x
#             return acc
#         return helper
#     return f()

# acc = 1
# def make_accumulator():
#     acc = 2
#     def f():
#         def helper(x):
#             global acc  # this will result in the acc = 2 being used
#             acc += x
#             return acc
#         return helper
#     return f()

### DO NOT MODIFY THIS ###
A = make_accumulator()
B = make_accumulator()

######################################
# Question 3: Make Monitored! Part 1 #
######################################

def make_monitored(f):
    counter = 0
    def mf(arg):
        nonlocal counter
        if arg == 'how-many-calls?':
            return counter
        elif arg == 'reset-count':
            counter = 0
        else:
            counter += 1
            return f(arg)
    return mf

def make_monitored(f):
    counter = 0
    def mf(*args):
        nonlocal counter
        if args == 'how-many-calls?':
            return counter
        elif args == 'reset-count':
            counter = 0
        else:
            counter += 1
            return f(*args)
    return mf

# decorator: function wrapper
@make_monitored
def func(x):
    return x + 1

### DO NOT MODIFY THIS ###
def double(x):
    return 2 * x

d = make_monitored(double)

#######################################
# Question 5: Monte Carlo integration #
#######################################
import random
def make_monte_carlo_integral(P,x1,y1,x2,y2):
    total = 0
    inside = 0
    def helper(msg, arg*):
        nonlocal total
        nonlocal inside
        if msg == 'trials':
            return total
        elif msg == 'get estimate':
            area = (x2 - x1) * (y2 - y1)
            ratio = inside / total
            return area * ratio
        elif msg == 'run trials':
            for i in range(arg[0]):
                x = random.uniform(x1, x2)
                y = random.uniform(y1, y2)
                if p(x,y):
                    inside += 1
            total += arg[0]
    return helper

### DO NOT MODIFY THIS ###
import math
import random

def circle(x,y):
    return math.sqrt(x*x+y*y) < 1

circle_estimate = make_monte_carlo_integral(circle,-1,-1,1,1)

### The inrange function in testcases is used to check whether a value lies in a specified range.

####################################
# Question 6: Translations! Part 1 #
####################################

def translate(source,destination,string):
    d = {}
    for i in range(len(source)):
        d[source[i]] = destination[i]
    lst = list(string)
    for i in range(len(lst)):
        lst[i] = d.get(lst[i], lst[i])
    return " ".join(lst)

def translate(source,destination,string):
    d = {}
    for i in range(len(source)):
        d[source[i]] = destination[i]
    return " ".join(map(lambda c: d.get(c, c), string))

def translate(source,destination,string):
    d = dict(zip(list(source), list(destination)))
    return " ".join(map(lambda c: d.get(c, c), string))

def translate(source,destination,string):
    d = dict(zip(map(ord, source), map(ord, destination)))
    return string.translate(d)

####################################
# Question 7: Translations! Part 2 #
####################################

from string import ascii_lowercase as lower, ascii_uppercase as upper

def caesar_cipher(shift, string):
    shift = shift % 26
    source = lower + upper
    destination = lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift]
    return translate(source, destination, string)