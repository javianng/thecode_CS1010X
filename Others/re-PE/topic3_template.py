class Node(object):
    def __init__(self, num, before, after, top, bottom):
        self.num = num
        self.before = before    # node before the current node
        self.after = after      # node after the current node
        self.top = top          # its copy above the current layer
        self.bottom = bottom    # a copy below the current layer

def insert_into(head, num):
    if head == None:
        # this is the very first node in the list
        return Node(num, None, None, None, None)

    previous = None
    current = head
    while current != None:
        if num < current.num:
            # insert newNode before the current node
            newNode = Node(num, previous , current, None, None)
            if previous != None:
                previous.after = newNode
            if current.before == None:
                head = newNode
            current.before = newNode
            return head
        previous = current
        current = current.after
    # insert newNode after the last node in the current list
    newNode = Node(num, previous, None, None, None)
    previous.after = newNode
    return head
    
lst = None
for i in [4,3,16,14,24,2,5,22,17,9,1,6,11,7,18,12,13]:
    lst = insert_into(lst, i)

########################################
# Question 8 : print routine
#

def all_keys(node):
    pass

# print("Current full list is:", all_keys(lst))
# Current full list is: 1-2-3-4-5-6-7-9-11-12-13-14-16-17-18-22-24

######################################
# Question 9: find in one level
#
def search_layer(node, num):
    pass

print("Current full list is:", all_keys(lst))
for i in range(1,27,5):
    print( "visited nodes in searching for", i, ":", search_layer(lst, i) )


###############################
# creating layer above
#
import random
random.seed(1)          # let's use this seed for our testing
# input is a non-empty lst with the first element always smallest
def create_top(lst):
    topLst = Node(lst.num, None, None, None, lst)
    previous = topLst
    current = lst.after
    while current != None:
        rand = random.randint(0, 10)
        if rand <= 3:
            newNode = Node(current.num, previous, None, None, current)
            previous.after = newNode
            current.top = newNode
            previous = newNode
        current = current.after
    return topLst

topLst = create_top(lst)
print("Current topLst:", all_keys(topLst))

topMostLst = create_top(topLst)
print("Current topMostLst:", all_keys(topMostLst) )

################################
# Question 10: find
#
def search(topMostLst, num):
    pass

for i in range(26):
    print("searching", i, ":", search(topMostLst, i) )

