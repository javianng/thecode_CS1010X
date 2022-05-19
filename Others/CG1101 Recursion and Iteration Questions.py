#####################################
# Question 1: Legendre's Conjecture #
#####################################

def prime_number_checker(number):
    for n in range(2,int(number**0.5)+1):
        if number%n==0:
            return False
    return True

result = False

def legendre(n):
    if n == 0:
        global result 
        result = True
        return result
    else:
        inter_result = False
        for number in range(n**2, (n+1)**2):
            if prime_number_checker(number) == True:
                inter_result = True
                break
        if inter_result == True:
            return legendre(n-1)

# print(legendre(9))
# print(prime_number_checker(13))

###############################################
# Question 2: Legendre's Conjecture - Part 2! #
###############################################

