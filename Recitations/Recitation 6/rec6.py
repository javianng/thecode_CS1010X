# Question 1

many_things = [1, 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists ')]
# print ( many_things ) # [1, 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists ')]

numbers = [2, 3, 4] 
# print ( numbers ) # [2, 3, 4]

concatenated = many_things + numbers
# print ( concatenated ) # [1, 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists '), 2, 3, 4]

appended = many_things . append ( numbers )
# print ( appended ) # None
# print ( many_things ) # [1, 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists '), 2, 3, 4]

extended = many_things . extend ( numbers )
# print ( extended ) # None
# print ( many_things ) # [1, 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists '), [2, 3, 4], 2, 3, 4]

many_things [0] = 7
# print ( many_things ) # [7, 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists '), [2, 3, 4], 2, 3, 4]

can_be_indexed = concatenated [2]
# print ( can_be_indexed ) # ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists ')

can_be_indexed_multiple_times = concatenated [2][1]
# print ( can_be_indexed_multiple_times ) # can

a_shallow_copy = concatenated [:]
# print ( a_shallow_copy ) # [1, 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists '), 2, 3, 4]
# print ( a_shallow_copy == concatenated ) # True
# print ( a_shallow_copy is concatenated ) # False

woops = a_shallow_copy [2]
# print ( woops ) # ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists ')
# print ( woops is can_be_indexed ) # True

singleton = ['blah ']
# print ( singleton ) # ['blah ']

# Question 2