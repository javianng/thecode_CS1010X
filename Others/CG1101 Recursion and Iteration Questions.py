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
        for number in range(n**2, ((n+1)**2)+1):
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

def legendre_n(n):
    
    def prime_number_checker(number):
        for n in range(2,int(number**0.5)+1):
            if number%n==0:
                return False
        return True

    counter = 0
    
    for i in range (n**2, (((n+1)**2)-1)):
        if (prime_number_checker(i)) == True:
            counter += 1
    return counter

# print(legendre_n(3))

#####################################
# Question 3: Goldbach's Conjecture #
#####################################

# every even integer greater than 2 can be written as the sum of two primes.

def goldbach(n):
    def list_of_odd_primes(n):
        primes = list(range(2, n+1))
        for i in primes:
            j=2
            while i*j<= primes[-1]:
                if i*j in primes:
                    primes.remove(i*j)
                j=j+1
        primes.remove(2)
        return primes
    x, y = 0, 0
    result = 0
    if n % 2 == 0: # check for even n input
        prime = list_of_odd_primes(n)
        while result != n:
            for i in range(len(prime)):
                if result == n: 
                    return True
                x = prime[i]
                for j in range(len(prime)):
                    y = prime[j]
                    result = x + y
                    if result == n: break
    return False

print(goldbach(1000))

################################
# Question 4: Maclaurin Series #
################################

def maclaurin(x, n):
    def helper(x, n):
        if n == 1:
            return 1
        
        else:
            numerator = x ** (n-1)
            
            denominator = 1        
            for i in range(1, n):
                denominator = denominator * i
                
            value = numerator / denominator
            
            return value + helper(x, n-1)
    return round(helper(x,n),3)

# print(maclaurin(2, 10))

###############################
# Question 5: Conway Sequence #
###############################

def conway(n):
    if n in [1, 2]:
        return 1
    else:
        return conway(conway(n-1)) + conway(n - conway(n-1))

# print(conway(6))

#############################
# Question 6: Recursive Sum #
#############################

def recursive_sum(n):
    if n in [0, 1, 2]:
        return 1
    elif n % 2 == 0 and n >= 3:
        return recursive_sum(n-1) + recursive_sum(n-2) + recursive_sum(n-3)
    elif n % 2 == 1 and n >= 3:
        return recursive_sum(n-1) + recursive_sum(n-2)
    else:
        print("Error Occurred")