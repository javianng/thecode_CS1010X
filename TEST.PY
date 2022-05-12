###################
# Heading Function #
###################

def python_heading_imput(title):
    str_title = str(title)
    print("#" * (len(str_title) + 4))
    print("# " + str(title) + " #")
    print("#" * (len(str_title) + 4))

# python_heading_imput("")


def java_heading_imput(title):
    str_title = str(title)
    print("/" * (len(str_title) + 6))
    print("// " + str(title) + " //")
    print("/" * (len(str_title) + 6))

# java_heading_imput("Question 12: Arrays")

num_array = (3, 4, 6, 1, 0, 9, 8, 6, 2, 5)

def print_n(n):
    counter = 0
    for i in range(n):
        counter = counter + num_array[i]
    return counter