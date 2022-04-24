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

# def calculate(inputs):

#     # you may assume that the input is always valid, 
#     # i.e. you do not need to check that the stack has at 
#     # least 2 elements if you encounter an operator
    
#     # create calculation_list for calculation and storing of inspected elements
    
#     calculation_list = make_empty_stack()
#     reversed_inputs = list(inputs)
#     reversed_inputs.reverse()
    
#     # create a loop to decide on next move
    
#     for element in inputs:
        
#         if isinstance(peek_stack(reversed_inputs), int):
#             push_stack(calculation_list, peek_stack(reversed_inputs))
#             pop_stack(reversed_inputs)
            
#         elif isinstance(peek_stack(reversed_inputs), str):
#             first_element = pop_stack(calculation_list)
#             second_element = pop_stack(calculation_list)
            
#             if peek_stack(reversed_inputs) == '+':
#                 pop_stack(reversed_inputs)
#                 calculated_element = first_element + second_element
#                 push_stack(calculation_list, calculated_element)
                
#             elif peek_stack(reversed_inputs) == '*':
#                 pop_stack(reversed_inputs)
#                 calculated_element = first_element * second_element
#                 push_stack(calculation_list, calculated_element)
                
#             elif peek_stack(reversed_inputs) == '/':
#                 pop_stack(reversed_inputs)
#                 calculated_element = second_element / first_element
#                 push_stack(calculation_list, calculated_element)
#     return int(calculation_list[0])

def calculate(inputs):
    
    temporary_list = [] # to store the integers to be calculated and ultimately the answer to be returned
    
    for counter in range(len(inputs)):
        
        if isinstance(inputs[counter], int):
            
            # print("int: " + str(inputs[counter]))
            
            temporary_list.append(inputs[counter])
            
        elif isinstance(inputs[counter], str):
            
            # print("str detected")
            
            second_element = pop_stack(temporary_list)
            first_element = pop_stack(temporary_list)
            
            # print("first element: " + str(first_element))
            # print("second element: " + str(second_element))
            
            if inputs[counter] == "+":
                calculated_element = second_element + first_element
                push_stack(temporary_list, calculated_element)
                
            elif inputs[counter] == "*":
                calculated_element = second_element * first_element
                push_stack(temporary_list, calculated_element)
                
            elif inputs[counter] == "/":
                calculated_element = first_element / second_element
                push_stack(temporary_list, calculated_element)
            
            elif inputs[counter] == "-":
                calculated_element = first_element - second_element
                push_stack(temporary_list, calculated_element)

    return int(temporary_list[0])

# print(calculate((5, 2, '/', 4, '*')))
# print(calculate((28, )))
# print(calculate((1, 2, '+', 3, '/')))