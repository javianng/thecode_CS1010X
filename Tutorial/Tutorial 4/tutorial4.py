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