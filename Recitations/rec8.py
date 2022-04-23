a = (("apple", 2), ("orange", 4), (5, 7))
b = dict(a)

c = [[1, 2], [3, 4], [5, 7]]
d = dict(c)

print(b["orange"]) 

# 4

print(b[5])

# 7

print(b[1])

# ("orange", 4)

b["bad"] = "better"
b[1] = "good"

for key in b.keys ():
    print(key)

for val in b.values ():
    print(val)

del b["bad"]
del b["apple"]

print(tuple(b.keys ()))

print(list(b.values ()))

######
# Q2 #
######

# i 

