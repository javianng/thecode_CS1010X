
from email.encoders import encode_quopri
from tokenize import String


plain = [ ['0','1','2','3','4','5'],
           ['6','7','8','9','A','B'],
           ['C','D','E','F','G','H'],
           ['I','J','K','L','M','N'],
           ['O','P','Q','R','S','T'],
           ['U','V','W','X','Y','Z'] ]

message = "HELLO 1 2 3"
# Q1
def encrypt(message, plain, c1, c2):
    result = ""
    
    plain_dict = {}
    
    c1_list = []
    c2_list = []
    
    for letter in c1:
        c1_list.extend(letter)
    for letter in c2:
        c2_list.extend(letter)
    
    for i in range(len(plain)):
        for j in range(len(plain[0])):
            plain_dict[plain[i][j]] = str(c1[i]) + str(c2[j])
    
    for letter in message:
        if letter == " ":
            result += " "
        else:
            result += str(plain_dict.get(letter))
        
    return result

secret = encrypt(message, plain, '062849', 'abcdef')
# print(secret)

# # Q2

def decrypt(secret, plain, c1, c2):
    
    def pairing(process_list):
        if len(process_list) == 0:
            return []
        elif process_list[0] == " ":
            return [" "] + pairing(process_list[1:])
        else:
            return [str(process_list[0]) + str(process_list[1])] + pairing(process_list[2:])
        
    process_list = []
    
    result = ""
    
    plain_dict = {}
    
    c1_list = []
    c2_list = []
    
    for letter in c1:
        c1_list.extend(letter)
    for letter in c2:
        c2_list.extend(letter)
    
    for i in range(len(plain)):
        for j in range(len(plain[0])):
            plain_dict[str(c1[i]) + str(c2[j])] = plain[i][j]
    
    for letter in secret:
        if letter == " ":
            process_list += [" "]
        else:
            process_list += letter
        
    process_list_2 = pairing(process_list)
    
    for element in process_list_2:
        if element == " ":
            result += " "
        else:
            result += str(plain_dict.get(element))
    
    return result

# print( decrypt(secret, plain, '062849', 'abcdef'))

# # Q3

lst_dict = {}


def index(lst, char):


lst = [0,[1,2,3]]
print(index(lst, 2))

# for i in range(11):
#     print("index of", i, "in", lst, "is:", index(lst, i))