# Dictionary to keep track of memoized data
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

# Question 1

# Question 2

def cut_rod(length_of_rod, dictionary_of_length_to_price):
    pass

# Test
prices = {1:1, 2:5, 3:8, 4:9, 5:10 , 6:17 , 7:17 , 8:20 , 9:24 , 10:30}
cut_rod (4, prices )