# Question 1 

# (a)

def collatz_distance(n):
    if n==1:
        return 0
    elif n%2==0:
        return 1+ collatz_distance(n/2)
    else:
        return 1+ collatz_distance(3*n+1)

# print(collatz_distance(6))

# (b)

def max_collatz_distance(n):
    maximum = 0
    for i in range(1,n+1):
        if collatz_distance(i) > maximum:
            maximum = collatz_distance(i)
    return maximum

# print(max_collatz_distance(11))

# (c)

# Dynamic programming doesn't work as there is no systematic approach to build the solution 
# from small to big.

memoize_table = {}

def memoize(f, name):
    if name not in memoize_table:
        memoize_table[name] = {}
    table = memoize_table[name]
    def helper(*args):
        if args in table:
            return table[args]
        else:
            result = f(*args)
            table[args] = result
            return result
    return helper

def collatz_distance_memo(n):
    def helper(n):
        if n==1:
            return 0
        elif n%2==0:
            return 1+ collatz_distance_memo(n/2)
        else:
            return 1+ collatz_distance_memo(3*n+1)
    return memoize(helper, "collatz_distance")(n)

def max_collatz_distance_memo(n):
    def helper(n):
        maximum = 0
        for i in range(1,n+1):
            if collatz_distance_memo(i) > maximum:
                maximum = collatz_distance_memo(i)
        return maximum
    return memoize(helper, "max_collatz_distance_memo")(n)

# print(collatz_distance_memo(6))
# print(max_collatz_distance_memo(6))
# print(max_collatz_distance_memo(8))

# (d)

def max_collatz_distance_memo(n):
    maximum=0
    helper_dict= {}

    def helper(n):
        if n in helper_dict:
            return helper_dict[n]
        elif n==1:
            return 0
        elif n%2==0:
            result= 1+ helper(n/2)
            helper_dict[n]=result
            return result
        else:
            return 1+ helper(3*n+1)
            helper_dict[n]=result
            return result

    for i in range(1,n+1):
        if helper(i)>maximum:
            maximum=helper(i)

    return maximum

# print(max_collatz_distance_memo(6))

# Question 2

from urllib.request import urlopen
from urllib.parse import urlsplit
from urllib.error import *

class InternetFail(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
def httpget(url):
    parsed = urlsplit(url)
    print(parsed)
    if not parsed.scheme:
        url = "https://" + url
    elif parsed.scheme != "http" and parsed.scheme != "https":
        raise ValueError(" Unknown protocol ")
    try:
        return urlopen(url).read()
    except HTTPError as err:
        raise InternetFail("Internet Fail  " + str(err))
    except URLError as err:
        raise ValueError("Value Error " + str(err))


URLS = [["", "impossible.txt"]] #, ["http://google.com.cs1010fc", "fail.text"] ["https://coursemology.org", "coursemology.txt"]]

def download_URLs(URL_filenames):
    for url in URL_filenames:
        try:
            contents = httpget(url[0])
            with open(url[1], 'wb') as myfile:
                myfile.write(contents) 
        except (InternetFail, ValueError) as err:
            print("could not access " + url[0] + " : " + str(err))