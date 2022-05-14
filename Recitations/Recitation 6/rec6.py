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

def bubble(lst):
    for j in range(len(lst)-1):
        for i in range(len(lst)-1-j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]

# Time Complexity: O(n**2)
# Space Complexity: O(1) # 2 extra variables required
# Between bubble with "for i in range(len(lst)-1-j):"" and bubble with "for i in range(len(lst)-1):"
# the first version is faster but their time complexity is the same.

# Question 3

def selection(lst):
    for i in range in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

# Time Complexity: O(n**2)
# Space Complexity: O(1) # 2 extra variables required

# Question 4

students = [
('tiffany ', 'A', 15),
('jane ', 'B', 10),
('ben ', 'C', 8),
('simon ', 'A', 21),
('john ', 'A', 15),
('jimmy ', 'F', 1),
('charles ', 'C', 9),
('freddy ', 'D', 4),
('dave ', 'B', 12 )]

# a

# >>> students.sort (key=lambda x:x[0], reverse=True)

# b

# >>> students.sort (key=lambda x:x[0])
# >>> students.sort (key=lambda x:x[1])

# c

# Method 1

# >>> a = tuple(filter(lambda x: len(x[0]) < 6, students))
# >>> tuple(map(lambda x:x[0], a))

# Method 2

# >>> a = tuple(map(lambda x: x[0], students))
# >>> tuple(filter(lambda x: len(x) < 6, a))

# d

def count(students): 
    grades = tuple(map(lambda x: x[1], students)) # returns a tuple of just the grades
    def count_freq(grades): # solving via recursion
        if grades == (): 
            return () 
        else: 
            first = grades[0] # obtaining the first grade
            count = len(tuple(filter(lambda x: x == first, grades))) # filter to get only the desired grade and count them
            rest = tuple(filter(lambda x: x != first, grades)) # get remaining grades tuple
            return ((first, count),) + count_freq(rest) # recursively add grade and its count
    return count_freq(grades)