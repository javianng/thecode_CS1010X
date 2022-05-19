#####################################
# Question 1: Legendre's Conjecture #
#####################################

def legendre(n):
    
    pass

def prime_number_checker(number):
    if number > 1:
    # check for factors
        for i in range(2,number):
            if (number % i) == 0:
                return False
            else:
                return True
    else:
        return False