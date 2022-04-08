def calc_integral(f, a, b, n):

    h = (b-a)/n
    
    for counter in range(n):
        
        if counter == 0 and counter == n:
            return 1
        
        elif counter%2 == 0:
            return 4
        
        else:
            return 2
        
    return 