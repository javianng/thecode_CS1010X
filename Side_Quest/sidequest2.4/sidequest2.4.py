#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

##########
# Task 1 #
##########

# Simplifed Order notations:

# 4^n * n^2
# Ans: 4^n

# n * 3^n
# Ans: 3^n

# 1000000000n^2
# Ans: n^2

# 2^n/1000000000
# Ans: 2^n

# n^n + n^2 + 1
# Ans: n^n

# 4^n + 2^n
# Ans: 4^(n)

# 1^n
# Ans: 1

# n^2
# Ans: n^2

# Faster order of growth in each group:

# i. n * 3^n
# ii. 1000000000n^2
# iii. n^n + n^2 + 1
# iv. n^2

##########
# Task 2 #
##########

# Time complexity: O(n)
# Space complexity: O(n)

##########
# Task 3 #
##########

# Time complexity of bar: O(n)
# Time complexity of foo: O(n^2)

# Space complexity of bar: O(n)
# Space complexity of foo: O(n^2)

def bar(n):
    if n == 0:
        return 0
    else :
        return n + bar(n - 1)

def foo(n):
    if n == 0:
        return 0
    else :
        return bar(n) + foo(n - 1)

def improved_foo(params):
    return int((params**3)/6 + (params**2)/2 + params/3)

# print(foo(11))

# Improved time complexity: O(1)
# Improved space complexity: O(1)