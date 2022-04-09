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
    return [x, y]

def x_point(p):
    return p[0]
    
def y_point(p):
    return p[1]

#For running public test case, do not delete
p1 = make_point(2, 3)

# Question 7

def make_segment(p1, p2):
    return [p1,p2]
    
def start_segment(s):
    return s[0]

def end_segment(s):
    #Your code here
    return s[1]
    
#do not uncomment! this is for reference only.
p1 = make_point(2, 3)
p2 = make_point(5, 7)

# Question 8

'''Version 1

def midpoint_segment(segment):
    
    x_coor = (segment[0][0] + segment[1][0]) / 2
    y_coor = (segment[0][1] + segment[1][1]) / 2
    
    return make_point(x_coor, y_coor)
    
#for running public test case, do not delete!
p1 = make_point(2, 3)
p2 = make_point(5, 7)
s = make_segment(p1, p2)

print(midpoint_segment(s))'''


'''Version 2'''

def midpoint_segment(segment):
    start_point = start_segment(segment)
    end_point = end_segment(segment)

    mid_x = 0.5 * (x_point(start_point) + x_point(end_point))
    mid_y = 0.5 * (y_point(start_point) + y_point(end_point))

    return make_point(mid_x, mid_y)

#for running public test case, do not delete!
p1 = make_point(2, 3)
p2 = make_point(5, 7)
s = make_segment(p1, p2)