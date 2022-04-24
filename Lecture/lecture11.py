##############
# Question 7 #
##############

def increase_by_one(d):
    
    if d == {}:
        return d
    
    else:
        temp_element = 0
        
        for key in d:
            if isinstance(d[key], dict):
                increase_by_one(d[key])
            
            else:    
                temp_element = d[key]                
                temp_element += 1
                d[key] = temp_element
    return d


# print(increase_by_one({ }))
# print(increase_by_one({'first':27, 'second':16, 'third':8}))
# print(increase_by_one({'1':2.7, '11':16, '111':{'a':5, 't':8}}))

##############
# Question 8 #
##############

def sum_all(*args):
    return sum(args)

# print(sum_all(1, 2, 3, 4, 5))