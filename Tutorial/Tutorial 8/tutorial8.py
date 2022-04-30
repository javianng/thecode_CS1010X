#######################
# Question 1: Widget! #
#######################

def make_widget():
    stuff = ["empty", "empty", 0]
    def oplookup(msg, *args):                         # *arg -> arbitrary number of arguements
        if msg == "insert":
            place = stuff[2]
            stuff[place] = args[0]
            stuff[2] = (place + 1) % 2
        elif msg == "retrieve":
            return stuff[stuff[2]]
        else:
            raise Exception("widget doesn’t " + msg)
    return oplookup

widget = make_widget()