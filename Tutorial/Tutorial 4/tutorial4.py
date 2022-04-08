# Question 1

def calc_integral(f, a, b, n):
    
    h = (b - a) / n

    counter, total = 0, 0
    
    while counter <= n:
        
        term = f(a + (counter * h))
        
        if counter == 0 or counter == n:
            total += term
            
        elif counter % 2 == 0:
            total += 2*term
            
        else:
            total += 4*term
            
        counter += 1

    return total * h / 3.0

# Question 2

def fold(op, f, n):
    if n == 0:
        return f(0)
    return op(f(n), fold(op, f, n-1))

def g(k):
    return fold(lambda x,y: x*y, lambda x: (x - ((x+1) ** 2)), k)

# print(g(0))
# print(g(3))
# print(g(8))

# Question 3

# 3(a)

def accumulate(combiner, base, term, a, next, b):
    
    if a > b:
        return base

    return combiner(term(a), accumulate(combiner, base, term, next(a), next, b))

# 3(b)

def accumulate(combiner, base, term, a, next, b):
    terms = ()

    # generate all the terms in reverse order
    
    while a <= b :
        terms = (term(a),) + terms
        a = next(a)

    # combine the terms
    
    result = base
    for term in terms:
        result = combiner(term, result)

    return result

# Question 4

def sum(term, a, next, b):
    return accumulate(lambda x,y: x+y, 0, term, a, next, b) 

# Question 5

def accumulate_iter(combiner, null_value, term, a, next, b):
    terms = ()

    # generate all the terms in reverse order
    
    while a <= b :
        terms = (term(a),) + terms
        a = next(a)

    # combine the terms
    
    result = null_value
    for term in terms:
        result = combiner(term, result)
        
    return result

# Question 6

def make_point(x, y):
    #Your code here
    return 

def x_point(p):
    #Your code here
    return 
    
def y_point(p):
    #Your code here
    return 

#For running public test case, do not delete
p1 = make_point(2, 3)
