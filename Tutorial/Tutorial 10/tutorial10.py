# Question 1 

# (a)
def collatz_distance(n):
    if n==1:
        return 0
    elif n%2==0:
        return 1+ collatz_distance(n/2)
    else:
        return 1+ collatz_distance(3*n+1)
    

# (b)
def max_collatz_distance(n):
    maximum=0

    for i in range(1,n+1):
        if collatz_distance(i)>maximum:
            maximum=collatz_distance(i)

    return maximum

# (c)

memoize_table = {}

# Dynamic programming doesn't work as there is no systematic approach to build the solution 
# from small to big.

def memoize(f, name):
    if name not in memoize_table:
        memoize_table[name]= {}
    table= memoize_table[name]
    def helper(*args):
        if args in table:
            return table[args]
        else: 
            result= f(*args)
            table[args]= result
            return result
    return helper

def max_collatz_distance(n):
    maximum=0
    for i in range(1,n+1):
        if collatz_distance(i)>maximum:
            maximum=collatz_distance(i)

    return maximum

collatz_distance_memo = memoize(collatz_distance, "cd")

# (d)

table = {}
count = 0
def collatz_distance(n):
    global count 
    count += 1
    if n == 1:
        return 0
    else:
        if n in table:
            return table[n]
        else:
            cc = collatz_distance(f(n)) + 1
            table[n] = cc
            return cc

def max_collatz_distance(n):
    result=0
    for i in range(1,n+1):
        cd = collatz_distance(i)
        if cd > result:
            result = cd
    return result

# Question 2

from urllib.request import urlopen
from urllib.parse import urlsplit
from urllib.error import *
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
    
class InternetFail(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

URLS = [["", "impossible.txt"], ["http://google.com.cs1010fc", "fail.text"] ["https://coursemology.org", "coursemology.txt"]]
    
def download_URLs(URL_filenames):
    for url in URL_filenames:
        try:
            contents = httpget(url[0])
            with open(url[1], 'wb') as myfile:
                myfile.write(contents) 
        except (InternetFail, ValueError) as err:
            print("could not access " + url[0] + " : " + str(err))