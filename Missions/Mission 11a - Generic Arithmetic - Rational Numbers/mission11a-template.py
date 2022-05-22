#
# CS1010X --- Programming Methodology
#
# Mission 11a
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <your collaborator's matric> <your collaborator's name>

###############
# Mission 11a #
###############

##########
# Task 1 #
##########

# With these operations, compound generic operations can be defined, such as
# def square(x):
#   return mul(x, x)

# (a) What are the types of the input and output of the generic square operation?
# Answer: Generic-Ord

# (b) Why would we prefer to define square in the above way, rather than:
# def square(x):
#    return apply_generic("square", x)
# Answer: When you use the above method, we would have to define the square function
#         for all the different number package . However, when you use the method below,
#
#         def square (x):
#             return mul(x, x)
#
#         it can be used for all types of number package since it calls mul, which has already been 
#         defined for all previous number package. As such, when there is a different number package  
#         to be defined, the square function will inherit from the mul function and hence there is 
#         no need to redefine the square function for the new number pacakge package.

##########
# Task 2 #
##########

# In the ordinary number package, a generic number operator is indexed by the
# name of the operator and a tuple of strings. For example, the add operator is
# indexed by ’add_ord’ and (’ordinary’, ’ordinary’); negation is indexed by
# ’negate_ord’ and (’ordinary’, ).
# In contrast, the constructor that creates an ordinary number is indexed by
# ’make_ord’ and just a string ’ordinary’. Explain why we have such a difference.

# Hint: Consider the differences in the process of the creation of a Generic-Num,
# such as create_ordinary, and the operations we can apply on Generic-Num, such
# as add. How is make_ord invoked, and how is add_ord invoked?

# Answer: The generic number operator returns the apply_generic function, which uses a map function
# to retrieve a tag from the generic number and returns a tuple. Thus, they are indexed by the name 
# of the operator and a tuple of strings. However, the  constructor doesn't call the apply_generic and 
# doesn't create a tuple out of the string.

##########
# Task 3 #
##########

# There’s a right way and a wrong way to create a generic rational number. Here are two tries at
# producing 9/10. Which is the right way?

# first_try = create_rational(9, 10)
# second_try = create_rational(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce 9/10 and 3/10 and then try to add
# them? Why does this happen?

# Right way: second_try = create_rational(create_ordinary(9), create_ordinary(10))
# What happens: Exception: ('Bad tagged datum -- type_tag ', 9)
# Why it happens: 9 and 10 are untagged in the first_try. This means that the generic operator will 
#                 not be able to operate on the numbers, leading to exception.

##########
# Task 4 #
##########

# Produce expressions that define r2_7 to be the generic rational number whose numerator part is
# 2 and whose denominator part is 7, and r3_1 to be the generic rational number whose numerator
# is 3 and whose denominator is 1. Assume that the expression
# >>> csq = square(sub(r2_7, r3_1))
# is evaluated. Draw a box and pointer diagram that represents csq.

# As an example, the following is a box and pointer diagram that represents x, a Generic-
# Ord number:
# x = create_ordinary(5)
#
#         +---+---+---+---+
# x  -->  |       |       |
#         +---+---+---+---+
#             |       |
#             v       v
#         "ordinary"  5

# FILL IN YOUR ANSWERS HERE:
# r2_7 = create_rational(create_ordinary(2), create_ordinary(7))
# r3_1 = create_rational(create_ordinary(3), create_ordinary(1))

# csq = square(sub(r2_7, r3_1))

##
##            +---+---+---+---+---+---+       +---+---+---+---+
##  csg  -->  |       |       |       |  -->  |       |       |
##            +---+---+---+---+---+---+       +---+---+---+---+
##                |       |                       |       |
##                |       v                       v       v
##                |   +---+---+---+---+       "ordinary" "49"
##                |   |       |       |
##                |   +---+---+---+---+
##                |       |       |
##                v       v       v
##          "rational" "ordinary" 361
##

##########
# Task 5 #
##########

# Within the generic rational number package, the internal add_rat function
# handled the addition operation. Why is it not
# possible to name this function "add"?

# Answer: the function calls the generic function 'add'. if it was named 'add', it 
# would call itself causing an error.

##########
# Task 6 #
##########

from generic_arith import *

# Modify install_rational_package, indicating clearly your modifications.
def install_rational_package():
    def make_rat(x, y):
        return tag(reprat(x, y))
    def reprat(x, y):
        return (x, y)
    def numer(x):
        return x[0]
    def denom(x):
        return x[1]
    def tag(x):
        return attach_tag("rational", x)

    # add, sub, mul, div: (RepRat, RepRat) -> Generic-Rat
    def add_rat(x, y):
        return make_rat( add(mul(numer(x), denom(y)), mul(denom(x), numer(y))), mul(denom(x), denom(y)) )
    def sub_rat(x, y):
        return make_rat( sub(mul(numer(x), denom(y)), mul(denom(x), numer(y))), mul(denom(x), denom(y)) )
    def mul_rat(x, y):
        return make_rat( mul(numer(x), numer(y)), mul(denom(x), denom(y)) )
    def div_rat(x, y):
        return make_rat( mul(numer(x), denom(y)), mul(denom(x), numer(y)) )
    
    ## Amendments ##
    def negate_rat(x):
        # RepRat --> Generic-Rat
        return make_rat(negate(numer(x)), denom(x))
    def is_zero_rat(x):
        # RepRat --> Boolean
        return is_zero(numer(x))
    def is_eq_rat(x, y):
        # RepRat --> Boolean
        return is_equal(div(numer(x), denom(x)), div(numer(y), denom(y)))
    
    put("make", "rational", make_rat)
    put("add", ("rational", "rational"), add_rat)
    put("sub", ("rational", "rational"), sub_rat)
    put("mul", ("rational", "rational"), mul_rat)
    put("div", ("rational", "rational"), div_rat)
    
    ## Amendments ##
    put("negate", ("rational",), negate_rat)
    put("is_zero", ("rational",), is_zero_rat)
    put("is_equal", ("rational", "rational"), is_eq_rat)
    
install_rational_package()

def create_rational(x, y):
    return get("make", "rational")(x, y)

# Change the values for the test variables below
r1_2 = create_rational(create_ordinary(1), create_ordinary(2))
r2_4 = create_rational(create_ordinary(2), create_ordinary(4))
r1_8 = create_rational(create_ordinary(1), create_ordinary(8))

#################
# Do not change #
#################
def gradeThis():
    if is_equal(sub(r1_2, mul(r2_4, r1_2)), add(r1_8, r1_8)):
        print("Well done!")
    else:
        print("Please check your solution.")

gradeThis()