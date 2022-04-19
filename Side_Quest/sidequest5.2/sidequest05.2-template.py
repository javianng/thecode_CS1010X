#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from ast import pattern
from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def kochize(level):
    
    if level == 0:
        return unit_line
    
    else:
        a = kochize(level-1)
        b = connect_ends(rotate(pi/3)(a), rotate(-pi/3)(a))
        c = put_in_standard_position(connect_ends(connect_ends(a, b), a))
        return c

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))

#show_connected_koch(0, 4000)
#show_connected_koch(4, 4000)

##########
# Task 2 #
##########

def snowflake():
    return connect_ends(connect_ends(rotate(2*pi/3)(kochize(5)), kochize(5)), rotate(-2*pi/3)(kochize(5)))

#draw_connected_scaled(10000, snowflake())