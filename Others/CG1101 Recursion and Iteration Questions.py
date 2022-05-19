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

# def eratosthenes(n):
#     primes = list (range(2, n+1))
#     for i in primes:
#         j=2
#         while i*j<= primes[-1]:
#             if i*j in primes:
#                 primes.remove(i*j)
#             j=j+1
#     return primes

# def odd_primes(N):
#     oddprimes = eratosthenes(N)
#     oddprimes.remove(2)
#     return(oddprimes)

# def goldbach(N):
#     x, y = 0, 0
#     result = 0
#     if N % 2 == 0:
#         prime = odd_primes(N)
#         while result != N:
#             for i in range(len(prime)):
#                 if result == N: break 
#                 x = prime[i]
#                 for j in range(len(prime)):
#                     y = prime[j]
#                     result = x + y
#                     if result == N: break 
#     return x, y 

# print(goldbach(4))

################################
# Question 4: Maclaurin Series #
################################

def maclaurin(x, n):
    # code that approximates e^x up to the nth term
    pass