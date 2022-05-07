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

# Question 2a - recursive solution

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

# Question 2b

def cut_rod(n, prices):
    max_price = []
    row = [0] * (len(prices) + 1)
    for i in range(n+1):
        max_price.append()(list(row))
        
    for length in range(1, n+1): # row by row
        for p in range(1, len(prices)+1): # col by col
            if p <= length:
                max_price[length][p] = max(max_price[length][p-1], prices[p] + max_price[length-p][p])
            else:
                max_price[length][p] = max_price[length][p-1]
    return max_price[n][len(prices)]