# Question 3: Making the Stack

def make_stack(seq):
    return list(seq)

def make_empty_stack():
    return []

def is_empty_stack(stack):
    return [] == stack


##########################################
#       Do not modify test code          #              
##########################################
s1 = make_empty_stack()                  #
s2 = make_stack((2, 4, 5))               #
s3 = make_stack([3, 5, 7, 8])            #
                                         #
is_empty1 = is_empty_stack(s1) #True	 #
is_empty2 = is_empty_stack(s2) #False	 #
is_empty3 = is_empty_stack(s3) #False    #
##########################################

# Question 4: Stacking like Jenga

def push_stack(stack, item):
    # pushes an item onto the stack, returns the stack
    pass # your code here

def pop_stack(stack):
    # removes the top item of the stack, returns that item. If the stack is empty, it should return None.
    pass # your code here


##########################################
#       Do not modify test code          #              
##########################################
s = make_empty_stack()                   #
first = pop_stack(s) #None               #
                                         #
push_stack(s, 1)                         #
push_stack(s, 2)                         #
                                         #
second = pop_stack(s) #2                 #
third = pop_stack(s)  #1                 #
push_stack(s, 3)                         #
fourth = pop_stack(s) #3                 #
##########################################
