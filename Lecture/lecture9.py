def remove_extras(lst):
    lst.sort()
    
    corrected_list = []
    for i in lst:
        if i not in corrected_list:
            corrected_list.append(i)
    
    lst = corrected_list
    
    return lst
        
# # Do not remove the following code
# lst1 = [1, 5, 1, 1, 3]
# lst2 = [2, 2, 2, 1, 5, 4, 4]
# result1 = remove_extras(lst1)
# result2 = remove_extras(lst2)
# print(remove_extras(lst1))

##############
# Question 7 #
##############

from cgitb import small


def count_occurrences(lst, num):
    count = 0
    for item in lst:
        if item == num:
            count += 1
        if isinstance(item, list):
            count += count_occurrences(item, num)
    return count

# print(count_occurrences([1, [2, 1], 1, [3, [1, 3]], [4, [1], 5], [1], 1, [[1]]], 1))
# print(count_occurrences([1, [2, 1], 1, [3, [1, 3]], [4, [1], 5], [1], 1, [[1]]], 3))

##############################
# Question 8: Sorting Tuples #
##############################

# def sort_age(lst):
#     lst.sort(key=lambda x: x[1], reverse=True)
#     return lst

# Failed because cannot use .sort :(((
    
def sort_age(lst):
    if len(lst) < 2:  # Base case!
        return lst
    left = sort_age(lst[:len(lst)//2])
    right = sort_age(lst[len(lst)//2:])
    return merge(left,right)

def merge(left,right):
    results = []
    while left and right:
        if left[0][1] > right[0][1]:
            results.append(left[0])
            left.remove(left[0])
        else:
            results.append(right[0])
            right.remove(right[0])
    results.extend(left)
    results.extend(right)
    return results

# print(sort_age([("M", 23), ("F", 19), ("M", 30)]))
# print(sort_age([("F", 18), ("M", 23), ("F", 19), ("M", 30)]))

#####################################
# Question 9: Not-so-simple Sorting #
#####################################

def sort_by_gender_then_age(lst):
    male_list = []
    female_list = []
    
    for element in lst:
        if element[0] == "M":
            male_list.append(element)
        elif element[0] == "F":
            female_list.append(element)
    
    # print(male_list)
    # print(female_list)
    
    sorted_male_list = sort_age(male_list)
    sorted_female_list = sort_age(female_list)
    
    # print(sorted_male_list)
    # print(sorted_female_list)
    
    sorted_list = sorted_male_list + sorted_female_list
    return sorted_list
    
# print(sort_by_gender_then_age([("M", 23), ("F", 19), ("M", 30)]))
# print(sort_by_gender_then_age([("F", 18), ("M", 23), ("F", 19), ("M", 30)]))

################
# Question 10: #
################

# # a 
# [3, 6, 9, 12] * 2
# # b
# ([1, 2, 3, 4] * 3) * 2
# # c
# map(lambda x: x*3, [1, 2, 3, 4]*2)
# # d
# list(map(lambda x: x*3, (1, 2, 3, 4) * 2))
# # e
# [x * 3 for x in list(range(4))] * 2
# # f
# [i*3 for i in (3, 6) * 4]
# # g
# [3, 6, 9, 12, 3, 6, 9, 12, 3, 6, 9, 12, 3, 6, 9, 12] / 2 

###################################
# Question 11: Merge Sorted Lists #
###################################

def merge_lists(list1, list2):

    merged_list = []
    combined_list = list1 + list2

    while combined_list:
        largest = -1000
        for element in combined_list:
            if element > largest:
                largest = element
        combined_list.remove(largest)
        merged_list.append(largest)
        
    return merged_list


# print(merge_lists([4, 2, 1], [6, 5, 3]))

######################
# Question 12: Top K #
######################

def top_k(lst, k):
    
    top_k = []
    
    for counter in range(k):

        largest = -1000
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        top_k.append(largest)
                
    return top_k
    
# print(top_k([4, 5, 2, 3, 1, 6], 3))