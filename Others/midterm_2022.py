# Question 1: Warming Up

# A

z = lambda x: 1 if (x < 0 or x > 10) else (2 if x % 2==0 else 3) 
def f(a, b):
    sum = 0
    for i in range (a, b): 
        sum += z(i) 
    return sum 

# print (f(-6,16))

# B

t = (1,2,3,4) 
lst = [66, 77] 

def gn(c): 
    c[0] = [88] 
    c[1][1] = 55 
    return 

def fn(a, b): 
    m = [a,b] 
    a = b
    gn(m)
    return m

r = fn(t, lst)

# print(t)
# print(lst)
# print(r)

# Question 2: Something familiar first [4 marks]

def compose (f, g): 
    return lambda x:f(g(x)) 

def twice (f): 
    return compose (f, f) 

def thrice (f): 
    return compose (f, compose (f, f)) 

def repeated (f, n): 
    if n == 0: 
        return identity 
    else: 
        return compose (f, repeated (f, n - 1))     

add1 = lambda x: x + 1
identity =  lambda x: x

# print (twice (thrice) (add1) (1))
# print (twice (thrice) (twice) (add1) (1))
# print (thrice (twice) (thrice (add1)) (1))
# print (twice (thrice) (repeated(thrice (add1), 100)) (1))

# Question 3: Not really unfamiliar [9 marks]

# A