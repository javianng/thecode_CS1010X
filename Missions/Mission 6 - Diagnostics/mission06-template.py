#
# CS1010X --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:

# Mission 5

# Task 3

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

# left curve, right curve
# rotate ( theta )( arg_curve )

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn), rotate(-theta)(curve_fn)))
    return inner_gosperize

# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(1000)(0.1), 500)

# Choose a significant level for testing for all three sets of functions.

def repeat_five_times(function):
    sum = 0
    for i in range(5):
        print(function)
        sum += function
    print(sum)
    
repeat_five_times(profile_fn(lambda : gosper_curve(1000)(0.1), 10))

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

# print("gosper_curve: " + str(profile_fn ( lambda : gosper_curve(1000)(0.1), 10)))
# print("gosper_curve: " + str(profile_fn ( lambda : gosper_curve(1000)(0.1), 10)))
# print("gosper_curve: " + str(profile_fn ( lambda : gosper_curve(1000)(0.1), 10)))
# print("gosper_curve: " + str(profile_fn ( lambda : gosper_curve(1000)(0.1), 10)))
# print("gosper_curve: " + str(profile_fn ( lambda : gosper_curve(1000)(0.1), 10)))

# Time measurements
# 62.684000000000005
# 60.78900000000001
# 64.174
# 59.576000000000015
# 61.65599999999999
# average: 61.7758


# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# print("gosper_curve_with angle: " + str(profile_fn ( lambda : gosper_curve_with_angle(1000, lambda lvl : pi/4)(0.1), 10)))
# print("gosper_curve_with angle: " + str(profile_fn ( lambda : gosper_curve_with_angle(1000, lambda lvl : pi/4)(0.1), 10)))
# print("gosper_curve_with angle: " + str(profile_fn ( lambda : gosper_curve_with_angle(1000, lambda lvl : pi/4)(0.1), 10)))
# print("gosper_curve_with angle: " + str(profile_fn ( lambda : gosper_curve_with_angle(1000, lambda lvl : pi/4)(0.1), 10)))
# print("gosper_curve_with angle: " + str(profile_fn ( lambda : gosper_curve_with_angle(1000, lambda lvl : pi/4)(0.1), 10)))

# Time measurements
# 60.57800000000002
# 61.255
# 58.466000000000015
# 59.49299999999996
# 59.33200000000005
# average: 59.8248

#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# print("your_gosper_curve_with_angle: " + str(profile_fn ( lambda : your_gosper_curve_with_angle(1000, lambda lvl : pi/4)(0.1), 10)))
# print("your_gosper_curve_with_angle: " + str(profile_fn ( lambda : your_gosper_curve_with_angle(1000, lambda lvl : pi/4)(0.1), 10)))
# print("your_gosper_curve_with_angle: " + str(profile_fn ( lambda : your_gosper_curve_with_angle(1000, lambda lvl : pi/4)(0.1), 10)))
# print("your_gosper_curve_with_angle: " + str(profile_fn ( lambda : your_gosper_curve_with_angle(1000, lambda lvl : pi/4)(0.1), 10)))
# print("your_gosper_curve_with_angle: " + str(profile_fn ( lambda : your_gosper_curve_with_angle(1000, lambda lvl : pi/4)(0.1), 10)))

# Time measurements
# 89500.75799999999
# 90054.23499999999
# 89625.61099999999
# 93246.70499999996
# 90659.35999999999
# average: 90617.3338

# Conclusion:
# customizerbility does not affect the speed at which the function is computed.
# gosper_curve and gosper_curve_with_angle both run at about the same time despite
# the latter having the additional angle variable. gosper_curve_with_angle and 
# your_gosper_curve_with_angle run at drastically different time despite having the
# same number of variables. thus customizability is not the factor that affects the 
# time taken

##########
# Task 2 #
##########

#  1) they both work the same as and achieve the same purpose.


#  2) joe_rotate function has to call the function curve(t) repeatedly in 
#     "x, y = x_of(curve(t)), y_of(curve(t))" as compared to once when it is 
#     directly being assigned to the variabe "pt".

##########
# Task 3 #
##########

#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1         <03>           <04>
#                      2         <05>           <10>
#                      3         <07>           <22>
#                      4         <09>           <46>
#                      5         <11>           <94>
#
#  Evidence of exponential growth in joe_rotate.
