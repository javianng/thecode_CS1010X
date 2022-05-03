# Question 1

def at_least_n(lst, n):
    for i in range(len(lst)):
        if lst[i] < n:
            print(lst[i])
            lst.remove(lst[i])
    return lst

# lst = list(range(10)) 
# print(lst)
# lst2 = at_least_n(lst, 5) 
# print(lst2)

# The implementation is incorrect as he is amending the list while iterating through it.
# As he iterates through the list, take lst for exmaple. The "0" removed will result in
# "1" being in index position 0 and not be processed and removed from the list. Also,
# there will no longer be an element at index position 9 in the list since there are lesser
# elements, resulting in an error when the for loop looks for an element at that postion.

# Question 2

def at_least_n(lst,n):
    for i in lst:
        print(i)
        if i < n:
            lst.remove(i)
    return lst

# lst = list(range(10)) 
# print(lst)
# lst2 = at_least_n(lst, 5) 
# print(lst2)

# No. Moral of the story is not to amend a list while iterating through it.

def at_least_n(lst, n):
    correct_list = []
    for element in lst:
        if element >= n:
            correct_list.append(element)
    lst.clear()
    lst.extend(correct_list)
    return lst

### DO NOT MODIFY THIS ###
lst1 = list(range(10))  
lst2 = list(range(8))
lst3 = list(range(6,10))

# print(at_least_n(lst1, 5))
# print(at_least_n(lst1, 5) == [5, 6, 7, 8, 9])
# print(at_least_n(lst3, 5))

# Question 4

def at_least_n(lst, n):
    correct_list = []
    for element in lst:
        if element >= n:
            correct_list.append(element)
    return correct_list

### DO NOT MODIFY THIS ###
lst1 = list(range(10))  
lst2 = list(range(8))
lst3 = list(range(6,10))

# print(at_least_n(lst1, 5))
# print([5, 6, 7, 8, 9])
# print(at_least_n(lst1, 5) == [5, 6, 7, 8, 9])

# Question 5

def col_sum(matrix):
    return list(map(sum, zip(*matrix)))

def col_sum(matrix):
    
    number_of_columns = len(matrix)
    number_of_rows = len(matrix[0])

    result = []
    processing = []
    
    for row_index in range(number_of_rows):
        for column_index in range(number_of_columns):
            processing.append(matrix[column_index][row_index])
        result.append(sum(processing))
        processing.clear()
    return result

# print(col_sum([[1,2],[3,4],[5,6]]))

# Question 6

def row_sum(matrix):
    
    result = []
    
    for list in matrix:
        result.append(sum(list))
    
    return result
    
# print(row_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))

# Question 7

def transpose(matrix):
    
    new_matrix = []
    
    for i in range(len(matrix[0])): 
        
        # iterate through each column in the original m
        row = list(map(lambda lst: lst[i], matrix)) 
        
        # finds the values from each column to form a list (a row in the transposed mat)
        new_matrix.append(row)
    
    matrix.clear()
    matrix.extend(new_matrix)
    
    return matrix

### DO NOT MODIFY THIS ###
matrix1 = [[ 1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[ 1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix3 = [[1, 2, 3]]

# print(transpose(matrix1))

# Question 8

"""Insertion sort (see mission)"""
# The unsorted elements are selected and placed into a sorted pile.

"""Selection sort (see lecture)"""
# The largest or smallest is choosen and then placed at the end of the list. This is then
# repeated for all the elements til they are sorted.

"""Bubble sort (see recitation)"""
# Bubble sort is a sorting algorithm that compares two adjacent elements and swaps 
# them until they are not in the intended order.

"""Merge sort (see lecture)"""
# The list is divided into two. Then each list is sorted individually. Then the two sorted lists are merged by
# selecting the smallest or largest between the two list.

# Question 9

def mode_score(students):
    
    # list to store score only
    sorted_score = []
    for student in students:
        sorted_score.append(student[2])
    sorted_score.sort()  # sort list in order
    
    # list with number of occurrence
    number_of_occurrence = []
    
    # loop through the entire list to return the number of occurrence of each element
    i = 0
    while i < len(sorted_score):
        number_of_occurrence.append(sorted_score.count(sorted_score[i]))
        i += 1
    
    # form a dictionary key, value pair between the element and its count
    dictionary_number_of_occurrence = dict(zip(sorted_score, number_of_occurrence))
    
    # return the highest number of occurrence 
    answer = [key for (key, value) in dictionary_number_of_occurrence.items() if value == max(number_of_occurrence)]
    return answer

### DO NOT MODIFY THIS ###
students = [('tiffany', 'A', 15), 
            ('jane', 'B', 10),
            ('ben', 'C', 8), 
            ('simon', 'A', 21), 
            ('eugene', 'A', 21), 
            ('john', 'A', 15), 
            ('jimmy', 'F', 1), 
            ('charles', 'C', 9), 
            ('freddy', 'D', 4), 
            ('dave', 'B', 12)]

# print(mode_score(students))

# Question 10

def top_k(students, k):
    
    # sort students in order of score
    sorted_students = sorted(students, key = lambda x:x[0])
    sorted_students = sorted(sorted_students, key = lambda x:x[2], reverse = True)
    
    # list to be returned
    top_k_list = []
    
    for counter in range(k):
        top_k_list.append(sorted_students[counter])
    
    # check if the next student has the same score as the previous student
    current_score = sorted_students[counter][2]
    
    for counter_ii in range(k, len(sorted_students)):
        if sorted_students[counter_ii][2] == current_score:
            top_k_list.append(sorted_students[counter_ii])
    
    return top_k_list

### DO NOT MODIFY THIS ###
students = [('tiffany', 'A', 15), 
            ('jane', 'B', 10),
            ('ben', 'C', 8), 
            ('eugene', 'A', 21),
            ('simon', 'A', 21), 
            ('john', 'A', 15), 
            ('jimmy', 'F', 1), 
            ('charles', 'C', 9), 
            ('freddy', 'D', 4), 
            ('dave', 'B', 12)]

# print(top_k(students,3))