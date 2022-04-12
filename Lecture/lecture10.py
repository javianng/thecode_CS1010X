# Question 3: Making the Stack

from logging import raiseExceptions
from re import S


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
    
    '''Pushes item onto the stack, returns the stack'''
    
    stack.append(item)
    return stack

def pop_stack(stack):
    
    '''removes the top item of the stack, returns that item. 
    If the stack is empty, it should return None.'''

    # for empty list
    
    if len(stack) == 0:
        return None
    
    else:
        index = len(stack)-1
        pop_item = stack.pop(index)
        return pop_item
    
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

# Question 5: Added Functionality

def peek_stack(stack):
    # returns but does not remove the top element of the stack. 
    # If the stack is empty, it should return None.
    if len(stack) == 0:
        return None
    else:
        index = len(stack) - 1
        return stack[index]
    
def clear_stack(stack):
    # modifies the stack to be empty and returns the stack
    stack.clear()
    return stack


##########################################
#       Do not modify test code          #              
##########################################
s1 = make_empty_stack()                  #
s2 = make_stack((2, 4, 5))               #
                                         #
peek1 = peek_stack(s1) #None             #
peek2 = peek_stack(s2) #5                #
                                         #
clear_stack(s2)                          #
peek3 = peek_stack(s2) #None             #
##########################################

# Question 6: The postfix expression

def calculate(inputs):
    # you may assume that the input is always valid, 
    # i.e. you do not need to check that the stack has at 
    # least 2 elements if you encounter an operator

    # create tuple_list for inputs and reverse it, allow for easier removal of elements
    
    tuple_list = make_stack(inputs)
    tuple_list.reverse()
    # print(tuple_list)
    
    # create calculation_list for calculation and storing of inspected elements
    
    calculation_list = make_empty_stack()
    # print(calculation_list)
    
    # create a loop to decide on next move
    
    while len(tuple_list) > 0:
        if isinstance(peek_stack(tuple_list), int):
            push_stack(calculation_list, peek_stack(tuple_list))
            pop_stack(tuple_list)
            # print("calculation_list: " + str(calculation_list))
            
        elif isinstance(peek_stack(tuple_list), str):
            first_element = pop_stack(calculation_list)
            # print("first_element: " + str(first_element))
            second_element = pop_stack(calculation_list)
            # print("second_element: " + str(second_element))
            
            if peek_stack(tuple_list) == '+':
                # print("+ detected")
                pop_stack(tuple_list)
                calculated_element = first_element + second_element
                # print("calculated_element: " + str(calculated_element))
                push_stack(calculation_list, calculated_element)
                # print("calculation_list: " + str(calculation_list))
                
            elif peek_stack(tuple_list) == '*':
                # print("* detected")
                pop_stack(tuple_list)
                calculated_element = first_element * second_element
                # print("calculated_element: " + str(calculated_element))
                push_stack(calculation_list, calculated_element)
                # print("calculation_list: " + str(calculation_list))
                
            elif peek_stack(tuple_list) == '/':
                pop_stack(tuple_list)
                calculated_element = first_element / second_element
                push_stack(calculation_list, calculated_element)
    return int(calculation_list[0])

print(calculate((5, 2, '/', 4, '*')))