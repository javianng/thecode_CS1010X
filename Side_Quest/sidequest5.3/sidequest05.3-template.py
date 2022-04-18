#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def yj_dragonize(num_points , curve):
    if num_points == 0:
        return curve
    else:
        c = yj_dragonize(num_points -1, curve)
        return put_in_standard_position(connect_ends(rotate(-pi/2)(c), c))


def dragonize(order, curve):
    if order == 0:
        return curve
    else:
        c = dragonize(order-1, curve)
        return put_in_standard_position(connect_ends(revert(c), rotate(pi/2)(c)))

def revert(curve):
    return lambda t: curve(1-t)

# test:
# draw_connected_scaled(4096, dragonize(12, unit_line))
# draw_connected_scaled(10, yj_dragonize(2 , unit_line))