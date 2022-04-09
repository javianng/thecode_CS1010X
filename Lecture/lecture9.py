def remove_extras(lst):
    lst.sort()
    
    corrected_list = []
    for i in lst:
        if i not in corrected_list:
            corrected_list.append(i)
    
    lst = corrected_list
    
    return lst
        
# Do not remove the following code
lst1 = [1, 5, 1, 1, 3]
lst2 = [2, 2, 2, 1, 5, 4, 4]
result1 = remove_extras(lst1)
result2 = remove_extras(lst2)