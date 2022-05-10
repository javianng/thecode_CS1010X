# Dictionary to keep track of memoized data
from operator import le


memoize_table = {}

def memoize(f, name): # name to allow us to reference table
    if name not in memoize_table: # if name not in dictionary, create a new dictionary in the dictionary
        memoize_table[name] = {}
    table = memoize_table[name] # this is not the memoize table but the dictionary in memoize table
    def helper(*args):
        if args in table:
            return table[args]
        else:
            result = f(*args) # compute result
            table[args] = result # put the result into the table with args as key i.e. store value
            return result
    return helper

# Question 1a

# A
# Start with writing cc
coins = [50, 20, 10, 5, 1]
count = 0

def cc(a, d):
    global count
    count += 1
    if a < 0 or d == 0:
        return 0
    elif a == 0:
        return 1
    else:
        return cc(a-coins[d-1], d) + cc(a, d-1)

# B
coins = [1, 5, 10, 20, 50]

# C

count2 = 0
seen = {}
def memo_cc(a, d):
    global count2
    count2 += 1
    if (a,d) in seen:
        return seen[(a,d)]
    
    if a < 0 or d == 0:
        return 0
    elif a == 0:
        return 1
    else:
        ans = memo_cc(a- coins[d-1], d) + memo_cc(a, d-1)
        seen[(a,d)] = ans
        return ans

# D

coins = [1, 5, 10, 20, 50]

# Complexity of memoization: O(a * d) + time taken by dictionary
# Space required is O(ad)

# Question 1b

coins = [1, 5, 10, 20, 50]

def dp_cc(a, d):
    table = []
    oneline = [0]*(d+1)
    for i in range(a+1):
        table.append(list(oneline))
    for i in range(1, d+1):
        table[0][i]=1
    
    for col in range(1, d+1): # col by col method
        for row in range(1, a+1):
            if (row - coins[col-1]) < 0:
                ans1 = 0
            else:
                ans1 = table[row-coins[col-1]][col]
            table[row][col] = ans1 + table[row][col-1]
            
    return table

def dp_cc(a, d):
    table = []
    oneline = [0]*(d+1)
    for i in range(a+1):
        table.append(list(oneline))
    for i in range(1, d+1):
        table[0][i]=1
    
    for i in range(1, a+1): # row by row method
        for j in range(1, d+1):
            if i - coins[j-1] >= 0:
                table[i][j] = table[i-coins[j-1]][j] + table[i][j-1]
            else:
                table[i][j] = table[i][j-1]
    return table

def print_table(table):
    for i in range(len(table)):
        print(i, " : ", table[i])

# print_table(dp_cc(100, 5))

# Question 2a - Recursive solution

def cut_rod(n, prices):
    if n <= 0:
        return 0
    else:
        max_price = 0
        for p in prices: # for p in prices.keys()
            if p <= n:
                max_price = max(max_price, prices[p] + cut_rod(n-p, prices))
        return max_price

# Test
# prices = {1:1, 2:5, 3:8, 4:9, 5:10 , 6:17 , 7:17 , 8:20 , 9:24 , 10:30}
# cut_rod (4, prices )

# Quesiton 2 - memo

seen = {}

def cut_rod(n, prices):
    if n in seen:
        return seen[n]
    
    if n <= 0:
        return 0
    else:
        max_price = 0
        for p in prices: # for p in prices.keys()
            if p <= n:
                max_price = max(max_price, prices[p] + cut_rod(n-p, prices))
        seen[n] = max_price
        return max_price

# Question 2b - Dynamic Programming # 1

def cut_rod(n, prices):
    max_price = []
    row = [0] * (len(prices) + 1)
    for i in range(n+1):
        max_price.append(list(row))
        
    for length in range(1, n+1): # row by row
        for p in range(1, len(prices)+1): # col by col
            if p <= length:
                max_price[length][p] = max(max_price[length][p-1], prices[p] + max_price[length-p][p])
            else:
                max_price[length][p] = max_price[length][p-1]
    return max_price[n][len(prices)]

prices1 = {10:30, 9:24, 8:20, 7:17, 6:17, 5:10, 4:9, 3:8, 2:5, 1:1}
prices2 = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}
print(cut_rod(10, prices1) == 30)
print(cut_rod(10, prices2) == 30)
print(cut_rod(20, prices1) == 60)
print(cut_rod(20, prices2) == 60)
print(cut_rod(100, prices1) == 300)

# Alternative

def cut_rod(n, prices):
    max_price = [0]*(n+1)
    for length in range(1, n+1):
        # by this time, all max_price(length-1), max_price(length-2) are
        # all correctly computed 
        # thus, in the for-loop with p, we can safely use them to calculate 
        # max_price[length]
        # this is to say that, max_price[length] in the below for-loop with p,
        # is just a temporary one
        for p in prices:
            if p <= n:
                max_price[length] = max(max_price[length], prices[p] + max_price[length-p])
        # then, at this point, the value of max_price[length] is corretly computed
    return max_price[n]