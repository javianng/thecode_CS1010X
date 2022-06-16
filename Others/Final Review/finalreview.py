# Question 1

def deep_reverse(lst):
    lst.reverse()
    for element in lst:
        if isinstance(element, list):
            deep_reverse(element)
    return (lst)

# print(deep_reverse([1,2,3,4]))
# print(deep_reverse([1,2,[3,4],[[5]],[6,[7,8],9]])) 
# print(deep_reverse([1, [[[2, 3, 4, 5],6 ], 7], 8, [9, 10, [11]]]))

# Question 2

def deep_sum(lst):
    result = 0
    for element in lst:
        if isinstance(element, list):
            result += deep_sum(element)
        else:
            result += element
    return result

# print(deep_sum([1, [[[2, 3, 4, 5],6 ], 7], 8, [9, 10, [11]]]))
# print(deep_sum([1, 2, [3, 4, [[5]], [[6], [7, 8], 9], 10]]))
# print(deep_sum([1,2,3,4]))

# Question 3

class Number(object):
    def __init__(self, num):
        self.num = num
    
    def value(self):
        '''returns the numerical value of the number'''
        return self.num
    
    def minus(self, subtractor):
        '''number minus number'''
        return Number(self.num - subtractor.value())
    
    def times(self, mulitplier):
        '''number times number'''
        return Number(self.num * mulitplier.value())
    
    def divide(self, divisor):
        '''number divide by divisor'''
        return Number(self.num / divisor.value())
    
    def plus(self, addition):
        '''number plus number'''
        return Number(self.num + addition.value())

# three=Number(3)
# ten=Number(10)
# seven=ten.minus(three)
# twentyone=seven.times(three)
# five=Number(5)
# two=ten.divide(five)

# Question 4

class Number(object):
    def __init__(self, num):
        self.num = num
    
    def value(self):
        '''returns the numerical value of the number'''
        return self.num
    
    def minus(self, subtractor):
        '''number minus number'''
        if self.value() == "Undefined" or subtractor.value() == "Undefined":
            return Number("Undefined")
        else:
            return Number(self.num - subtractor.value())
    
    def times(self, mulitplier):
        '''number times number'''
        if self.value() == "Undefined" or mulitplier.value() == "Undefined":
            return Number("Undefined")
        else:
            return Number(self.num * mulitplier.value())
    
    def divide(self, divisor):
        '''number divide by divisor'''
        if divisor.value() == 0 or self.value() == "Undefined" or divisor.value() == "Undefined":
            return Number("Undefined")
        else:
            return Number(self.num / divisor.value())
    
    def plus(self, addition):
        '''number plus number'''
        if self.value() == "Undefined" or addition.value() == "Undefined":
            return Number("Undefined")
        else:
            return Number(self.num + addition.value())

# seventeen = Number(17)
# four = Number(4)
# zero = Number(0)

# thirteen = seventeen.minus(four)
# fiftytwo = thirteen.times(four)

# blackjack=seventeen.plus(four)
# something=blackjack.divide(zero)
# another_thing=blackjack.plus(something)
# something_else=another_thing.divide(blackjack)

# Question 5

class Number(object):
    def __init__(self, num):
        self.num = num
    
    def value(self):
        '''returns the numerical value of the number'''
        return self.num
    
    def minus(self, subtractor):
        '''number minus number'''
        if self.value() == "Undefined" or subtractor.value() == "Undefined":
            return Number("Undefined")
        else:
            return Number(self.num - subtractor.value())
    
    def times(self, mulitplier):
        '''number times number'''
        if self.value() == "Undefined" or mulitplier.value() == "Undefined":
            return Number("Undefined")
        else:
            return Number(self.num * mulitplier.value())
    
    def divide(self, divisor):
        '''number divide by divisor'''
        if divisor.value() == 0 or self.value() == "Undefined" or divisor.value() == "Undefined":
            return Number("Undefined")
        else:
            return Number(self.num / divisor.value())
    
    def plus(self, addition):
        '''number plus number'''
        if self.value() == "Undefined" or addition.value() == "Undefined":
            return Number("Undefined")
        else:
            return Number(self.num + addition.value())
    
    def spell(self):
        def spell_function(num):
            if num > 10000000: 
                return "really large number"
            
            else:
                num_list = []
                for number in str(num):
                    num_list.append(int(number))
                num_list.reverse()
                num_list += [0] * (8-len(num_list))
                
                tens = num_list[:2]
                hundreds = [num_list[2]]
                ten_thousands = num_list[3:5]
                hundred_thousands = [num_list[5]]
                millions = num_list[6:8]
                
                def two_digit(lst):
                    '''combine two list with a single digit into one list'''
                    if lst[1] == 1:
                        lst[1] = int(str(lst[1]) + str(lst[0]))
                        lst[0] = 0
                    elif lst[0] == 0:
                        if lst[1] != 0:
                            lst[1] = int(str(lst[1]) + str(0))
                    elif lst[0] != 0:
                        if lst[1] != 0:
                            lst[1] = int(str(lst[1]) + str(0))
                    return lst
                
                two_digit(tens)
                two_digit(ten_thousands)
                
                def num_to_word(num):
                    '''turns the numbers into words'''
                    language_dict = {
                        1: "one ", 2: "two ", 3: "three ", 4: "four ", 5: "five ", 6: "six ", 7: "seven ", 8: "eight ", 9: "nine ", 10: "ten ", 
                        11: "eleven ", 12: "twelve ", 13: "thirteen ", 14: "fourteen ", 15: "fifteen ", 16: "sixteen ", 17: "seventeen ", 18: "eighteen ", 19: "nineteen ", 
                        20: "twenty ", 30: "thirty ", 40: "forty ", 50: "fifty ", 60: "sixty ", 70: "seventy ", 80: "eighty ", 90: "ninety ",
                        100: "hundred ", 1000: "thousand", 1000000: "million", 
                        "space": " ", "comma": ", ", "and": "and "
                    }
                    if num != 0:
                        return language_dict.get(num)
                
                # Insert the hundred, thousand, million, "comma" and "and" keyword
                
                if millions != [0,0]:
                    millions.insert(0, 1000000)
                    if hundred_thousands[0] != 0 or ten_thousands != [0,0] or hundreds[0] != 0 or tens != [0,0]:
                        millions.insert(0, "comma")
                if hundred_thousands[0] != 0:
                    hundred_thousands.insert(0, 100)
                    if ten_thousands != [0,0] or hundreds[0] != 0 or tens != [0, 0]:
                        hundred_thousands.insert(0, "and")
                if ten_thousands != [0,0] or hundred_thousands[0] != 0:
                    ten_thousands.insert(0, 1000)
                    if tens != [0, 0] or hundreds != [0]:
                        ten_thousands.insert(0, "comma")
                if hundreds[0] != 0:
                    hundreds.insert(0, 100)
                    if tens != [0, 0]:
                        hundreds.insert(0, "and")
                
                int_final_list = tens + hundreds + ten_thousands + hundred_thousands + millions
                int_final_list.reverse()
                
                word_final_list = []
                
                for element in int_final_list:
                    if element != 0:
                        word_final_list.append(num_to_word(element))
                
                result = ""
                
                for word in word_final_list:
                    result += str(word)
                    
                return result.rstrip()
        return spell_function(self.num)

# elite_number=Number(1337)
# good_day_number=Number(210792)
# bigno=good_day_number.times(elite_number)

# elite_number.spell()
# good_day_number.spell()
# bigno.spell()

# Question 6

def power_set(lst):
    result = [[]]
    for x in lst :
        newsubsets = [subset + [x] for subset in result]
        result.extend(newsubsets)
    return result

# print(power_set([1,2,3]))

# Question 7

def power_set_check(lst):
    flatten_lst = []
    for element in lst:
        for sub_element in element:
            flatten_lst.append(sub_element)
    original_elements = list(set(flatten_lst)) # seek out base elements
    correct_power_set = power_set(original_elements) # seek out correct power set
    
    # sort list for comparison
    
    return sorted(lst) == sorted(correct_power_set)
    
# print(power_set_check([[1,2,3],[1,2],[1,3],[2,3],[1],[2],[3],[]]))
# print(power_set_check([[1,2,3]]))
# print(power_set_check([[], ['lugia'], ['ho-oh'], ['ho-oh' , 'lugia']]))
# print(power_set_check([[1, 2, 3]]))
# print(power_set_check([[1,2,3],[1,2],[1,3],[2,3],[1],[2],[3],[]]))

# Question 8

def enumerate_interval(min, max):
    return list(range(min, max+1))

def map(fn, seq):
    if seq == []:
        return []
    else:
        return [fn(seq[0]),] + map(fn, seq[1:])

def filter(pred, seq):
    if seq == []:
        return []
    elif pred(seq[0]):
        return [seq[0],] + filter(pred, seq[1:])
    else:
        return filter(pred, seq[1:])

def accumulate(fn, initial, seq):
    if seq == []:
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))

# Leave your answers below   
    
def part_i():
    '''code for [1, 2, 3, 4, 5, 6, 7, 8]'''
    return enumerate_interval(1,8)

# print(part_i())

def part_ii():
    '''code for [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]'''
    return filter(lambda x: x%5==0, enumerate_interval(5, 60))

# print(part_ii())

def part_iii():
    '''code for [1, 9, 25, 49, 81, 121]'''
    return map(lambda x: x ** 2, filter(lambda x: x%2 == 1, enumerate_interval(1,11)))

# print(part_iii())

def part_iv():
    '''code for [1, 1, 9, 2, 25, 3, 49, 4, 81, 5]'''
    list1 = map(lambda x: x ** 2, filter(lambda x: x%2 == 1, enumerate_interval(1,9)))
    list2 = enumerate_interval(1,5)
    list_combined = []
    for i in range(len(list1)):
        list_combined.append(list1[i])
        list_combined.append(list2[i])
    return list_combined

# print(part_iv())

def part_v():
    '''code for [20, 16, 14, 10, 8, 4, 2]'''
    10,8,7,5,4,2,1
    list1 = map(lambda x: x*2, filter(lambda x: x%3 != 0, enumerate_interval(1,10)))
    list1.reverse()
    return list1

# print(part_v())

# Question 9

def make_stack():
    stack = []
    def helper(keyword, *arg):
        if keyword == 'push':
            return stack.extend(arg)
        elif keyword == "pop":
            if not stack:
                return None
            return stack.pop()
        elif keyword == "peek":
            if not stack:
                return None
            return stack[-1]
        elif keyword == "size":
            return len(stack)
    return helper
    
# stk=make_stack()
# stk('push',1)
# stk('push',2)
# stk('push',3)
# stk('peek')
# print(stk('pop'))

# Question 10

# def prefix_infix(lst):
#     if isinstance(lst[1], list):
#         return "(" + prefix_infix(lst[1]) + " " + lst[0] + " " + prefix_infix (lst[2]) + ")"
#     return "(" + str(lst[1]) + " " + lst[0] + " " + str (lst[2]) + ")"

def prefix_infix(lst):
    if isinstance(lst, list):
        op, left, right = lst
        return '(' + prefix_infix(left) + " " + op + " " + prefix_infix(right) + ')'
    else:
        return str(lst)

def prefix_infix(lst): 
    stk=make_stack() 
    def helper(lst):
        if type(lst)==int: 
            stk('push',str(lst))
        elif lst in ('+','-','*','/'): 
            left=stk('pop')
            right=stk('pop')
            element="("+left+" "+lst+" "+right+")"
            stk('push',element)
        else:
            return helper(lst[2]),helper(lst[1]),helper(lst[0]) 
    helper(lst)
    return stk('pop')

# print(prefix_infix(['+',['*',5,4],['-',2,1]]))
# print(prefix_infix(['-',['*',5,4],['-',['/',1,45],['+',1,1]]]))

# Question 11

def bubble_sort(lst):
    # loop to access each array element
    for i in range(len(lst)):
        
        # loop to compare array elements
        for j in range(len(lst) - i - 1):
            
            # compare two adjacent elements
            # change > to < to sort in descending order
            if lst[j] > lst[j + 1]:
                
                # swapping elements if elements
                # are not in the intended order
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

# print(bubble_sort([5,3,2,6,7,8,1,4]))

# Question 12

def split(n,lst):
    above_n_list = []
    below_n_list = []
    for element in lst:
        if element <= n:
            below_n_list.append(element)
        else:
            above_n_list.append(element)
    return [below_n_list, above_n_list]

# print(split(5,[1,10,4,9,7,2,5,8,3,4,9,6,2]))