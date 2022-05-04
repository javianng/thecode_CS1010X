# Question 1

import code


def accumulate(op, init, seq):
    if not seq:
        return init
    else:
        return op(seq[0], accumulate(op, init, seq[1:]))
    
def accumulate_n(op, init, sequences):
    if (not sequences) or (not sequences[0]):
        return type(sequences)()
    else :
        return ([accumulate(op, init, [element[0] for element in sequences])] + accumulate_n(op , init , [sublist[1:] for sublist in sequences]))
    
# print(accumulate_n(lambda x,y: x+y, 0, [[1,2],[3,4],[5,6]]))

# Question 2

def col_sum(m):
    return accumulate_n(lambda x,y : x+y, 0, m)

### DO NOT EDIT ANYTHING BEYOND THIS LINE. FOR YOUR REFERENCE ONLY! ###

def accumulate(op, init, seq):
    if not seq:
        return init
    else:
        return op(seq[0], accumulate(op, init, seq[1:]))

def accumulate_n(op, init, sequences):
    if (not sequences) or (not sequences[0]):
        return type(sequences)()
    else:
        return ([accumulate(op, init, list((map(lambda x: x[0], sequences))))] + accumulate_n(op, init, list((map(lambda x: x[1:], sequences)))) )

# print(col_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])) # [22, 26, 30]

# Question 3: Matrices! Part 2

def transpose(m):
    new_mat = []
    for i in range(len(m[0])): 
        row = list(map(lambda lst: lst[i], m)) 
        new_mat.append(row)
    return new_mat

def row_sum(m):
    return accumulate_n(lambda x, y: x + y, 0, transpose(m))
    
#### DO NOT EDIT ANYTHING BEYOND THIS LINE. FOR YOUR REFERENCE ONLY ####

def accumulate(op, init, seq):
    if not seq:
        return init
    else:
        return op(seq[0], accumulate(op, init, seq[1:]))

def accumulate_n(op, init, sequences):
    if (not sequences) or (not sequences[0]):
        return type(sequences)()
    else:
        return ( [accumulate(op, init, list((map(lambda x: x[0], sequences))))] + accumulate_n(op, init, list((map(lambda x: x[1:], sequences)))))

# print(row_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])) # [6, 15, 24, 33]
# print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])) # [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]

# Question 4: English! Part 1

def count_sentence(sentence):
    
    word_count = len(sentence)
    letter_count = 0
    
    # count letters w/o spaces
    for word in sentence:
        for letter in word:
            letter_count += 1
    
    # add spaces 
    letter_count = letter_count + word_count - 1
    
    return [word_count, letter_count]
    
# Order of growth?: O(l+w) where l is the number of letters and w is the number of words

#### DO NOT EDIT ANYTHING BEYOND THIS LINE. IT IS FOR YOUR REFERENCE ONLY!
def accumulate(op, init, seq):
    if not seq:
        return init
    else:
        return op(seq[0], accumulate(op, init, seq[1:]))

def accumulate_n(op, init, sequences):
    if (not sequences) or (not sequences[0]):
        return type(sequences)()
    else:
        return ( [accumulate(op, init, list((map(lambda x: x[0], sequences))))]  + accumulate_n(op, init, list((map(lambda x: x[1:], sequences)))))

# print(count_sentence([['C', 'S', '1', '0', '1', '0', 'S'], ['R', 'o', 'c', 'k', 's']])) # [2, 13]

# Question 5: English! Part 2

def letter_count(sentence):
    
    sorted_letters = []
    
    for word in sentence:
        for letter in word:
            sorted_letters.append(letter)
    sorted_letters.sort() # sort list in order
    
    # list with number of occurrence
    number_of_occurrence = []
    
    # loop through the entire list to return the number of occurrence of each element
    i = 0
    while i < len(sorted_letters):
        number_of_occurrence.append(sorted_letters.count(sorted_letters[i]))
        i += 1
        
    # form a dictionary key, value pair between the element and its count
    dictionary_number_of_occurrence = dict(zip(sorted_letters, number_of_occurrence))
    
    return list(map(list,dictionary_number_of_occurrence.items()))

# Order of growth?: O(4n) where n is the number of letters

# print(letter_count([['C', 'S', '1', '0', '1', '0', 'S'], ['R', 'o', 'c', 'k', 's']]))

# Question 6: English! Part 3

def most_frequent_letters(sentence):
    
    sorted_letters = []
    
    for word in sentence:
        for letter in word:
            sorted_letters.append(letter)
    sorted_letters.sort() # sort list in order
    
    # list with number of occurrence
    number_of_occurrence = []
    
    # loop through the entire list to return the number of occurrence of each element
    i = 0
    while i < len(sorted_letters):
        number_of_occurrence.append(sorted_letters.count(sorted_letters[i]))
        i += 1
        
    # form a dictionary key, value pair between the element and its count
    dictionary_number_of_occurrence = dict(zip(sorted_letters, number_of_occurrence))
    
    # return the highest number of occurrence 
    answer = [key for (key, value) in dictionary_number_of_occurrence.items() if value == max(number_of_occurrence)]
    
    return answer
    
# Order of growth?: O(4n) where n is the number of letters

# print(set(most_frequent_letters([['C', 'S', '1', '0', '1', '0', 'S'], ['R', 'o', 'c', 'k', 's']])))

# Question 7: Stacking

def make_queue():
    return []

def enqueue(q, item):
    q += [item]
    return q

def dequeue(q):
    return_element = q[0]
    q.remove(q[0])
    return return_element
    
def size(q):
    return len(q)
    
### DO NOT MODIFY BEYOND THIS LINE!
q = make_queue()
enqueue(q, 1)
enqueue(q, 5)

# Question 8: A Bomb Game

def who_wins(m, players):
    players_queue = make_queue()
    for player in players:
        enqueue(players_queue, player)
        
    while size(players_queue) > m-1:
        for counter in range(m):
            enqueue(players_queue, dequeue(players_queue))
        players_queue.remove(players_queue[0])
        
    return players_queue

# print(who_wins(3, ['val', 'hel', 'jam', 'jin', 'tze', 'eli', 'zha', 'lic']))
# print(who_wins(2, ['poo', 'ste', 'sim', 'nic', 'luo', 'ibr', 'sie', 'zhu']))