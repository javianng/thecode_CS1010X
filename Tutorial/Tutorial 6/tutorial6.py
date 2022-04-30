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

print(transpose(matrix1))

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

