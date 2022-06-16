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

elite_number=Number(1337)
good_day_number=Number(210792)
bigno=good_day_number.times(elite_number)

elite_number.spell()
good_day_number.spell()
bigno.spell()

# Question 6

def power_set(lst):
    result = [[]]
    for x in lst:
        newsubsets = [subset + [x] for subset in result]
        result.extend(newsubsets)
    return result

print(power_set([1,2,3]))