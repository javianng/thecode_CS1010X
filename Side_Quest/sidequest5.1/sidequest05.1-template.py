#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

# There is no visible difference between unit_circle and alternative_unit_circle when 
# draw_connected is used. However, the difference is observed when draw_points is used.
# The points in unit_circle is equaly spaced while in alternative_unit_circle, it increases 
# exponentially in distance.This is because the points (sin(2*pi*t),cos(2*pi*t)) and 
# (sin(2*pi*t*t),cos(2*pi*t*t)) can be connected by the same circle, thus resulting in 
# identical draw_connected circle. However, the points in unit_circle has a linearly increasing 
# value of t, which the points in alternative_unit_circle correspond to t ** 2, which increases
# exponentially.

##########
# Task 2 #
##########

# (a)
def spiral(t):
    return make_point(t*sin(2*pi*t), t*cos(2*pi*t))

# draw_connected_scaled(1000, spiral)

# (b)
def heart(t):
    return connect_rigidly(spiral, scale_xy(-1, 1)(spiral))(t)

# draw_connected_scaled(1000, heart)
