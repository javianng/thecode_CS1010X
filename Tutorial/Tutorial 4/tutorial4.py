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

def accumulate(combiner, base, term, a, next, b):
    return 
