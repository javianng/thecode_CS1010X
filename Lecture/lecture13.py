####################################
# Question 1: Normalizing a vector #
####################################

def normalize(lst):
    s = sum(lst)
    return list(map(lambda v: v / s, lst))

def safe_normalize(lst):
    try:
        return normalize(lst)
    except ZeroDivisionError:
        return lst

# print(safe_normalize([1, 2, 2, 3]))
# print(safe_normalize([1, 2, -5, 2]))

##########################################
# Question 2: Differentiating exceptions #
##########################################

def calculate(num):
    pass

def safe_calculate(num):
    try:
        return calculate(num)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return None

##################################
# Question 3: Raise an exception #
##################################

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False

def is_valid(d, m, y):
    # d, m, y represents day, month, and year in integer.
    if y < 1970 or y > 9999:
        return False
    if m <= 0 or m > 12:
        return False
    if d <= 0 or d > 31:
        return False

    if m == 4 or m == 6 or m == 9 or m == 11:
        if d > 30:
            return False

    if is_leap_year(y):
        if m == 2 and d > 29:
            return False
    else:
        if m == 2 and d > 28:
            return False
        
    return True

def get_day_month_year(date):
    split_date = date.split("/")
    d = int(split_date[0])
    m = int(split_date[1])
    y = int(split_date[2])
    return (d, m, y)

def less_than_equal(start_day, start_mon, start_year, end_day, end_mon, end_year):    
    if (start_year, start_mon, start_day) <= (end_year, end_mon, end_day):
        return True
    return False

def next_date(d, m, y):
    if m in (1, 3, 5, 7, 8, 10):
        if d == 31:
            return (1, m+1, y)
        return (d+1, m, y)
    if m == 12:
        if d == 31:
            return (1, 1, y+1)
        return (d+1, m, y)
    if m in (4, 6, 9, 11):
        if d == 30:
            return (1, m+1, y)
        return (d+1, m, y)
    if m == 2:
        if is_leap_year(y) == True:
            if d == 29:
                return (1, m+1, y)
            return (d+1, m, y)
        else:
            if d == 28:
                return (1, m+1, y)
            return (d+1, m, y)

def count_days(start_date, end_date):
    # date is represented as a string in format dd/mm/yyyy
    start_day, start_mon, start_year = get_day_month_year(start_date)
    end_day, end_mon, end_year = get_day_month_year(end_date)

    # if start date is not valid...
    
    if is_valid(int(start_day), int(start_mon), int(start_year)) == False:
        raise Exception("Not a valid date: " + start_date)
    
    # if end date is not valid...
    
    if is_valid(int(end_day), int(end_mon), int(end_year)) == False:
        raise Exception("Not a valid date: " + end_date)
    
    # if start date > end date...
    
    if less_than_equal(start_day, start_mon, start_year, end_day, end_mon, end_year) == False:
        raise Exception("Start date must be less than or equal end date.")
    
    # lazy - let the computer count from start date to end date
    count = 0
    while less_than_equal(start_day, start_mon, start_year, end_day, end_mon, end_year):
        count = count + 1
        start_day, start_mon, start_year = next_date(start_day, start_mon, start_year)

    # exclude end date
    return count - 1

# print(get_day_month_year('1/1/1999'))
# print(less_than_equal(19, 3, 2014, 19, 3, 2014))
# print(less_than_equal(18, 3, 2014, 19, 3, 2014))
# print(less_than_equal(20, 3, 2014, 19, 3, 2014))
# print(next_date(1, 1, 2013))
# print(next_date(28, 2, 2012))
# count_days('1/1/1970', '31/12/1969')
# count_days('19/3/2014', '19/4/2013')

########################################
# Question 4: Pascal Triangle DP Style #
########################################

def pascal(row, col):
    if col == 1 or col == row:
        return 1
    else:
        return pascal(row - 1, col) + pascal(row - 1, col - 1)

# print(pascal(9, 5)) # 70

def faster_pascal(row, col):
    table = []
    one_line = [0] * (col+1)
    for i in range(row+1):
        table.append(list(one_line))
    
    table[1][1] = 1 
    
    for i in range(1, row):
        for j in range(col):
            table[i+1][j+1] = table[i][j] + table[i][j+1]
    
    return table[row][col]
    
    # print table #
    
    # for i in range(len(table)):
    #     print(i, " : ", table[i])

# print(faster_pascal(9, 5))