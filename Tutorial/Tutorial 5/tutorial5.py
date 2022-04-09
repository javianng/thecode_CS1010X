# Question 1

tup = (7, (6, 5, 4), 3, (2, 1))

exp = tup[3][1]
# print(exp)

# Question 2

tup = (7, (6,), (5, (4,)), (3, (2, (1,))))

exp = tup[3][1][1][0]
# print(exp)

# Question 3

tup = ((7), (6, 5, 4), (3, 2), 1)

exp = tup[3]
# print(exp)

# Question 4

tup = (7, ((6, 5), (4,), 3, 2), ((1,),))

exp = tup[2][0][0]
# print(exp)

# Question 5

def even_rank(tup):
    
    result = []
    
    for counter in range(1,len(tup), 2):
        result.append(tup[counter])
    
    return tuple(result)
        
# print(even_rank((3, 1, 4, 3, 2, 3, 19, 7, -90)))
# print(even_rank((2,)))

# Question 6

def even_rank(tup):
    
    result = []
    
    for counter in range(1,len(tup), 2):
        result.append(tup[counter])
    
    return tuple(result)

def odd_rank(tup):
    
    result = []
    
    for counter in range(0,len(tup), 2):
        result.append(tup[counter])
    
    return tuple(result)

def odd_even_sums(val):
    return (sum(odd_rank(val)), sum(even_rank(val)))

# print(odd_even_sums((1, 3, 2, 4, 5)))

# Question 7

def hanoi(n, src, des, aux): 
    if n == 1: 
        return ( (src, des),) 
    return hanoi (n-1, src, aux, des) + hanoi (1, src, des, aux) + hanoi (n-1, aux, des, src)