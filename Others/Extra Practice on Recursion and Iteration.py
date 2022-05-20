# Question 1: Infinite Loop!

def foobar(n):
    result = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            result += i
    return result

# Question 2: Factorial recursive

def factorial_recursive(n):
    """Calculates n! using recursion"""
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

# Question 3: Factorial Iteration

def factorial_iteration(n):
    """Calculates n! using iteration"""
    result = 1
    if n == 0:
        return result
    else:
        for counter in range(1, n+1):
            result *= counter
        return result

# Question 4: Exponentiation recursive

def exponentiation_recursive(x, e):
    """Calculates x^e using recursion"""
    if e == 0:
        return 1
    elif e == 1:
        return x
    else:
        return x * exponentiation_recursive(x, e-1)

# Question 5: Exponentiation iteration

def exponentiation_iteration(x, e):
    """Calculates x^e iteratively"""
    if e == 0:
        return 1
    result = x
    temp_result  = x
    for counter in range(1, e):
        result = result * temp_result
    return result

# Question 6: Occurrence

def occurrence(s1, s2):
    """Counts the number of occurrences of s2 in s1"""
    return s1.count(s2)

# Question 7: Star wars recursive

def star_wars_recursive(num_enemy_ships):
    """Take down enemy ships!!"""
    if num_enemy_ships == 0:
        return ''
    elif num_enemy_ships%2 == 1: # if odd
        return star_wars_recursive(num_enemy_ships-1) + "*-"
    elif num_enemy_ships%2 == 0: # if even
        return star_wars_recursive(num_enemy_ships-1) + "*--"
    else:
        print("Error")

# Question 8: Star wars iteration

def star_wars_iteration(num_enemy_ships):
    """Releases just enough pulses to take down enemy ships"""
    result = ""
    if num_enemy_ships == 0:
        return result
    else:
        for counter in range(num_enemy_ships):
            if counter%2 == 1: # if odd
                result += "*--"
            elif counter%2 == 0: # if even
                result += "*-"
        return result