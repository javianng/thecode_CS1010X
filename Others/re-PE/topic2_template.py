###########################################################
##
## Q4, Q5, Q6, Q7 - you are not allowed to use any import function

def print_matrix(matrix):
    for i in range(len(matrix)):
        print (matrix[i])

# Q4        

def make_row(starting_number, length):
    result = []
    for i in range(starting_number, length):
        result.append(i)
    if len(result) < length:
        for j in range(0, length - len(result)):
            result.append(j)
    return result

def make_rotation_matrix(m, n):
    matrix = []
    for i in range(m):
        matrix.append(make_row(i, n))
    return matrix

##print("* rotation *")
##print(" rotation 5x5")
##print_matrix(make_rotation_matrix(5,5))
##print("")
##print(" rotation 6x5")
# print_matrix(make_rotation_matrix(6,5))

# Q5

def make_row(length):
    row = []
    for i in range(length-1, 0, -1):
        row.append(i)
    for j in range(0, length):
        row.append(j)
    return row

def make_symmetrical_matrix(n):
    matrix = []
    default_row = make_row(n)
    for i in range(n, 0, -1):
        print(i)
        matrix.append(default_row[i-1:i-1+n])
    return matrix

##print("")
##print("* symmetrical *")
##print(" symmetrical 5x5")
# print_matrix(make_symmetrical_matrix(5))
##print("")
##print(" symmetrical 6x6")
##print_matrix(make_symmetrical_matrix(6))

# Q6
def make_concentric_matrix(m,n):
    matrix = []
    zero_line = [0] * n
    one_line = [0] + [1] * (n-2) + [0]
    two_line = [0] + [1] + [2] * (n-4) + [1] + [0]
    if m == 3:
        matrix.append(zero_line)
        matrix.append(one_line)
        matrix.append(zero_line)
        return matrix
    
    elif m == 4:
        matrix.append(zero_line)
        matrix.append(one_line)
        matrix.append(one_line)
        matrix.append(zero_line)
        return matrix
    
    else:
        matrix.append(zero_line)
        matrix.append(one_line)
        for i in range(m-4):
            matrix.append(two_line)
        matrix.append(one_line)
        matrix.append(zero_line)
        return matrix

##print("")
##print("* concentric *")
##print(" concentric 3x3")
##print_matrix(make_concentric_matrix(3,3))
##print("")
##print(" concentric 4x4")
# print_matrix(make_concentric_matrix(5,10))
##print("")
##print(" concentric 5x5")
##print_matrix(make_concentric_matrix(5,5))
##print("")
##print(" concentric 5x6")
##print_matrix(make_concentric_matrix(5,6))
##print("")
##print(" concentric 5x10")
##print_matrix(make_concentric_matrix(5,10))

# Q7

def make_row(length, case):
    row = []
    if case == True: # double centre
        for i in range(1, length):
            row.append(i)
        for j in range(length-1, 0, -1):
            row.append(j)
        return row
    else: # single centre
        for i in range(1, length-1):
            row.append(i)
        for j in range(length-1, 0, -1):
            row.append(j)
        return row

def make_diamond_matrix(m,n):
    matrix = []
    for i in range(int(n/2)):
        make_row()

##print("")
##print("* diamond *")
##print(" diamond 7x7")
##print_matrix(make_diamond_matrix(7,7))
##print("")
##print(" diamond 8x8")
##print_matrix(make_diamond_matrix(8,8))
##print("")
##print(" diamond 9x9")
print_matrix(make_diamond_matrix(8,8))
##print("")
##print(" diamond 7x8")
##print_matrix(make_diamond_matrix(7,8))
##print("")
##print(" diamond 8x7")
##print_matrix(make_diamond_matrix(8,7))
##print("")

