a = (("apple", 2), ("orange", 4), (5, 7))
b = dict(a)

c = [[1, 2], [3, 4], [5, 7]]
d = dict(c)

print(b["orange"]) 

# 4

print(b[5])

# 7

print(b[1])

# Traceback error

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

def make_stack():
    stuff = []
    def helper(op, *arg):
        if op == "is_empty":
            return stuff == []
        elif op == "push":
            return lambda x: stuff.append(x)
        elif op == "pop":
            if not stuff:
                return None
            return stuff.pop()
        elif op == "peek":
            if not stuff:
                return None
            return stuff[-1]
        elif op == "clear":
            stuff.clear()
        else:
            print("command not recognised")
    return helper

# Alternative

def manyArgs(*arg):
    print("I was called with ", len(arg), "arguements: ", arg)
    
def make_stack():
    stuff = []
    def helper(op, *arg):
        if op == "is_empty":
            return stuff == []
        elif op == "push":
            return stuff.extend(arg)
        elif op == "pop":
            if not stuff:
                return None
            return stuff.pop()
        elif op == "peek":
            if not stuff:
                return None
            return stuff[-1]
        elif op == "clear":
            stuff.clear()
        else:
            print("command not recognised")
    return helper

    
######
# Q3 #
######

def push_all(s, tup):
    for item in tup:
        s("push")(item)
    return s

######
# Q4 #
######

def pop_all(s):
    result = []
    while (not s("is_empt")):
        result.append(s("pop"))
    return result

######
# Q2 #
######

def make_calculator():
    stack = make_stack () # data structure
    ops = {'+':lambda x, y: x + y,
            '-':lambda x, y: x - y,
            '*':lambda x, y: x * y,
            '/':lambda x, y: x / y}
    
    def oplookup(msg, *arg): # algorithmm to interpret the msg
        if msg == "ANSWER":
            if stack("is_empty"):
                return "empty_stack"
            return stack("peek")
        elif msg == "NUMBER_IMPUT":
            return stack("push", arg[0])
        elif msg == "OPERATION_INPUT":
            op = arg[0]
            y = stack("pop")
            x = stack("pop")
            stack("push", ops[op](x,y))
        elif msg == "CLEAR":
            stack("clear")
        else:
            raise Exception("calculator doesn't" + msg)
    return oplookup

# c = make_calculator()
# print(c('ANSWER '))              # empty_stack
# print(c('NUMBER_INPUT ',4))      # pushed
# print(c('ANSWER '))              # 4
# print(c('NUMBER_INPUT ',5))      # pushed
# print(c('ANSWER '))              # 5
# print(c('OPERATION_INPUT ','+')) # pushed
# print(c('ANSWER '))              # 9
# print(c('NUMBER_INPUT ',7))      # pushed
# print(c('OPERATION_INPUT ','-')) # pushed
# print(c('ANSWER '))              # 2
# print(c('CLEAR '))               # cleared
# print(c('ANSWER '))              # empty_stack