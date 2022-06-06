#
# CS1010X --- Programming Methodology
#
# Sidequest 10.1 Template
#
# Note that written answers are commented out to allow us to run your #
# code easily while grading your problem set.

from random import *
from re import X
from puzzle import GameGrid

###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]

###########
# Task 1  #
###########

def new_game_matrix(n):
    
    matrix = []
    
    row = [0]*n
    
    for counter in range(n):
        matrix += [row]
    return matrix

def has_zero(mat):
    result = False
    for row in mat:
        for element in row:
            if element == 0:
                result = True
    return result

def add_two(mat):
    if has_zero(mat) == False:
        return mat
    else:
        zero_list = []
        for row_position in range(len(mat)):
            for element_position in range(len(mat[row_position])): # create a list with positions of all the zeros in mat
                if mat[row_position][element_position] == 0:
                    zero_list.append([row_position,element_position])
                    
        chosen_zero = zero_list[randint(0, len(zero_list)-1)]
        
        mat[chosen_zero[0]][chosen_zero[1]] = 2 # make zero two
        return mat

###########
# Task 2  #
###########

def win_state(mat):
    result = False # False means have not won
    for row in mat:
        for element in row:
            if element == 2048:
                result = True # True means won
    return result

def lose_state(mat):
    result = False # False means lose
    if has_zero(mat) == True: # there is a zero in the matrix -> not lost
        result = True
    else:
        for i in range(len(mat)-1): # number beside is the same number -> not lost
            for j in range(len(mat)-1):
                if mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]:
                    result = True
    return result
    
def game_status(mat):
    if lose_state(mat) == False:
        return 'lose'
    elif win_state(mat) == True:
        return 'win'
    else:
        return 'not over'

# print(game_status([[2, 0, 2, 4], [0, 2, 4, 2], [2, 4, 0, 4], [4, 2, 4, 0]]))
# print(game_status([[2, 4, 16, 4], [4, 2, 2, 2], [2, 4, 2, 4], [4, 2, 4, 8]]))
# print(game_status([[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]]))
# print(game_status([[2, 0, 2, 2], [0, 0, 0, 4], [4, 0, 8, 4], [2, 0, 0, 2048]]))

###########
# Task 3a #
###########

def transpose(mat):
    new_mat = []
    for i in range(len(mat[0])): 
        row = list(map(lambda lst: lst[i], mat)) 
        new_mat.append(row)
    return new_mat

# print(transpose([[1, 2, 3], [4, 5, 6]]))

###########
# Task 3b #
###########

def reverse(mat):
    reversed_mat = [list(x) for x in mat]
    for i in reversed_mat:
        i.reverse()
    return reversed_mat

# print(reverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

############
# Task 3ci #
############

def merge_left(mat):
    
    increment = []
    
    def merge_left_row(row):
        result_row = []
        correct_len = len(row)
        
        def helper(row):
            current_tile = row[0]
            if len(row) == 1: # if one last element, add to current tile
                result_row.append(current_tile)
            elif len(row) == 0: # if no elements, end helper
                return []
            elif current_tile == 0: # for all cases of 0, the next number is then considered
                return helper(row[1:len(row)])
            elif len(row) == 2: # if two elements left to consider
                next_tile = row[1]
                if current_tile == next_tile:
                    result_row.append(current_tile*2)
                    increment.append(current_tile*2)
                elif current_tile != next_tile:
                    result_row.append(current_tile)
                    return helper(row[1:len(row)])
            elif len(row) > 2:
                next_tile = row[1]
                if current_tile == next_tile: # if current = next, add them together and look at the rest
                    result_row.append(current_tile*2)
                    increment.append(current_tile*2)
                    return helper(row[2:len(row)])
                elif next_tile == 0: # if next = 0, consider current and the rest.
                    return helper([current_tile] + row[2:len(row)])
                elif current_tile != next_tile: # if next != 0 and current != next, consider rest and append current to result
                    result_row.append(current_tile)
                    return helper(row[1:len(row)])
            
        helper(row)
        result_len = len(result_row)
        number_of_zeros = correct_len - result_len
        result_row += [0]*number_of_zeros
        
        return result_row
    
    new_mat = []
    for row in mat:
        new_mat.append(merge_left_row(row))
    return (new_mat, new_mat != mat, sum(increment))

# print(merge_left([[2, 2, 0, 2], [4, 0, 0, 0], [4, 8, 0, 4], [0, 0, 0, 2]]))

#############
# Task 3cii #
#############

def merge_right(mat):
    
    reverse_mat = reverse(mat)
    
    increment = []
    
    def merge_left_row(row):
        result_row = []
        correct_len = len(row)
        
        def helper(row):
            current_tile = row[0]
            if len(row) == 1: # if one last element, add to current tile
                result_row.append(current_tile)
            elif len(row) == 0: # if no elements, end helper
                return []
            elif current_tile == 0: # for all cases of 0, the next number is then considered
                return helper(row[1:len(row)])
            elif len(row) == 2: # if two elements left to consider
                next_tile = row[1]
                if current_tile == next_tile:
                    result_row.append(current_tile*2)
                    increment.append(current_tile*2)
                elif current_tile != next_tile:
                    result_row.append(current_tile)
                    return helper(row[1:len(row)])
            elif len(row) > 2:
                next_tile = row[1]
                if current_tile == next_tile: # if current = next, add them together and look at the rest
                    result_row.append(current_tile*2)
                    increment.append(current_tile*2)
                    return helper(row[2:len(row)])
                elif next_tile == 0: # if next = 0, consider current and the rest.
                    return helper([current_tile] + row[2:len(row)])
                elif current_tile != next_tile: # if next != 0 and current != next, consider rest and append current to result
                    result_row.append(current_tile)
                    return helper(row[1:len(row)])
            
        helper(row)
        result_len = len(result_row)
        number_of_zeros = correct_len - result_len
        result_row += [0]*number_of_zeros
        
        return result_row
    
    new_mat = []
    for row in reverse_mat:
        new_mat.append(merge_left_row(row))
    return (reverse(new_mat), reverse(new_mat) != mat, sum(increment))

# print(merge_right([[2, 2, 0, 2], [4, 0, 0, 0], [4, 8, 0, 4], [0, 0, 0, 2]]))

def merge_up(mat):
    
    transpose_mat = transpose(mat)
    
    increment = []
    
    def merge_left_row(row):
        result_row = []
        correct_len = len(row)
        
        def helper(row):
            current_tile = row[0]
            if len(row) == 1: # if one last element, add to current tile
                result_row.append(current_tile)
            elif len(row) == 0: # if no elements, end helper
                return []
            elif current_tile == 0: # for all cases of 0, the next number is then considered
                return helper(row[1:len(row)])
            elif len(row) == 2: # if two elements left to consider
                next_tile = row[1]
                if current_tile == next_tile:
                    result_row.append(current_tile*2)
                    increment.append(current_tile*2)
                elif current_tile != next_tile:
                    result_row.append(current_tile)
                    return helper(row[1:len(row)])
            elif len(row) > 2:
                next_tile = row[1]
                if current_tile == next_tile: # if current = next, add them together and look at the rest
                    result_row.append(current_tile*2)
                    increment.append(current_tile*2)
                    return helper(row[2:len(row)])
                elif next_tile == 0: # if next = 0, consider current and the rest.
                    return helper([current_tile] + row[2:len(row)])
                elif current_tile != next_tile: # if next != 0 and current != next, consider rest and append current to result
                    result_row.append(current_tile)
                    return helper(row[1:len(row)])
            
        helper(row)
        result_len = len(result_row)
        number_of_zeros = correct_len - result_len
        result_row += [0]*number_of_zeros
        
        return result_row
    
    new_mat = []
    for row in transpose_mat:
        new_mat.append(merge_left_row(row))
    return (transpose(new_mat), transpose(new_mat) != mat, sum(increment))

# print(merge_up([[2, 2, 0, 2], [4, 0, 0, 0], [4, 8, 0, 4], [0, 0, 0, 2]]))

def merge_down(mat):
    
    transpose_reverse_mat = reverse(transpose(mat))
    
    increment = []
    
    def merge_left_row(row):
        result_row = []
        correct_len = len(row)
        
        def helper(row):
            current_tile = row[0]
            if len(row) == 1: # if one last element, add to current tile
                result_row.append(current_tile)
            elif len(row) == 0: # if no elements, end helper
                return []
            elif current_tile == 0: # for all cases of 0, the next number is then considered
                return helper(row[1:len(row)])
            elif len(row) == 2: # if two elements left to consider
                next_tile = row[1]
                if current_tile == next_tile:
                    result_row.append(current_tile*2)
                    increment.append(current_tile*2)
                elif current_tile != next_tile:
                    result_row.append(current_tile)
                    return helper(row[1:len(row)])
            elif len(row) > 2:
                next_tile = row[1]
                if current_tile == next_tile: # if current = next, add them together and look at the rest
                    result_row.append(current_tile*2)
                    increment.append(current_tile*2)
                    return helper(row[2:len(row)])
                elif next_tile == 0: # if next = 0, consider current and the rest.
                    return helper([current_tile] + row[2:len(row)])
                elif current_tile != next_tile: # if next != 0 and current != next, consider rest and append current to result
                    result_row.append(current_tile)
                    return helper(row[1:len(row)])
            
        helper(row)
        result_len = len(result_row)
        number_of_zeros = correct_len - result_len
        result_row += [0]*number_of_zeros
        
        return result_row
    
    new_mat = []
    for row in transpose_reverse_mat:
        new_mat.append(merge_left_row(row))
    return (transpose(reverse(new_mat)), transpose(reverse(new_mat)) != mat, sum(increment))
    
# print(merge_down([[2, 2, 0, 2], [4, 0, 0, 0], [4, 8, 0, 4], [0, 0, 0, 2]]))

###########
# Task 3d #
###########

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return

# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
# text_play()

# How would you test that the winning condition works?
# Your answer: I would create a code that uses recursion to decide on the next move such that it
# makes the most logical move to possibly reach 2048. If the game ends at 2048, the winning condition 
# works.

##########
# Task 4 #
##########

def make_state(matrix, total_score):
    return (matrix, total_score)

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def make_new_game(n):
    return make_state(add_two(add_two(new_game_matrix(n))), 0)

def adder(result, state):
    if result[1] == True:
        return (make_state(add_two(result[0]), get_score(state) + result[2]), result[1])
    else:
        return (make_state(result[0], get_score(state) + result[2]), result[1])   

def left(state):
    result = merge_left(get_matrix(state))
    return adder(result, state)   

def right(state):
    result = merge_right(get_matrix(state))
    return adder(result, state)   

def up(state):
    result = merge_up(get_matrix(state))
    return adder(result, state)   

def down(state):
    result = merge_down(get_matrix(state))
    return adder(result, state)   

# Do not edit this #
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': lambda state: (state, False)
}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
#gamegrid = GameGrid(game_logic)

#################
# Optional Task #
#################

###########
# Task 5i #
###########

def make_new_record(mat, increment):
    return [mat, increment]

def get_record_matrix(record):
    return record[0]

def get_record_increment(record):
    return record[1]

############
# Task 5ii #
############

def make_new_records():
    return []

def push_record(new_record, stack_of_records):
    return [new_record] + stack_of_records

def is_empty(stack_of_records):
    return stack_of_records == []

def pop_record(stack_of_records):
    return stack_of_records[len(stack_of_records)-1]

#############
# Task 5iii #
#############

# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    return [matrix, total_score, records]

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def make_new_game(n):
    new_matrix = add_two(add_two(new_game_matrix(n)))
    return make_state(new_matrix, 0, [new_matrix])

def left(state):
    pass

def right(state):
    pass

def up(state):
    pass

def down(state):
    pass

# NEW FUNCTIONS TO DEFINE
def get_records(state):
    return state[2]

def undo(state):
    "Your answer here"

# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
##game_logic = {
##    'make_new_game': make_new_game,
##    'game_status': game_status,
##    'get_score': get_score,
##    'get_matrix': get_matrix,
##    'up': up,
##    'down': down,
##    'left': left,
##    'right': right,
##    'undo': undo
##}
#gamegrid = GameGrid(game_logic)