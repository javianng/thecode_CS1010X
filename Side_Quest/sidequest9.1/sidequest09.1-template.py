#
# CS1010X --- Programming Methodology
#
# Sidequest 9.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json
import time

#####################
# Reading json file #
#####################

def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google it :P

    For example, file.txt contains:
    [["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"], ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"], ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]]

    Calling read_json('file.txt') will return the following array
    [
        ["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"],
        ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"],
        ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]
    ]
    """
    datafile = open(filename, 'r', encoding='utf-8')
    return json.loads(datafile.read())

#############
# Accessors #
#############

def module_code(module):
    return module[0]

def module_name(module):
    return module[1]

def module_prof(module):
    return module[2]

###########
# Task 1a #
###########

def merge_lists(all_lst):
    
    final_list = []
    
    def checker():
        while [] in all_lst:
            all_lst.remove([])
        if len(all_lst) == 0:
            return False
        return True
    
    while checker():
        
        min_list = []
        
        for i in range(len(all_lst)):
            min_list.append(all_lst[i][0]) # append first element of each list
            # print("minlist: " + str(min_list))
            
        for i in range(len(min_list)):
            if min_list[i] == min(min_list):
                x = i # index of smallest element
        final_list.append(min(min_list)) # append smallest element to the final list
        # print("finallist: " + str(final_list))
        del all_lst[x][0] # remove the smallest element
        
    return final_list

all_lst = [[2, 7, 10], [0, 4, 6], [3, 11]]
# print("## Q1a ##")
# print(merge_lists(all_lst)) # [0, 2, 3, 4, 6, 7, 10, 11]

###########
# Task 1b #
###########

def merge(lists, field):
    
    final_list = []
    
    def checker(x):
        while [] in x:
            x.remove([])
        if len(x) == 0:
            return False
        return True
    
    while checker(lists):
        
        minimum = lists[0][0]
        number = 0
        
        for i in lists:
            # print("(i[0]): " + str(field(i[0])))
            # print("minimum: " + str(field(minimum)))
            if field(i[0]) < field(minimum): # comparing the first element of each list based on the criteria
                minimum = i[0]
                number = lists.index(i)       
                # print("minimum: " + str(field(minimum)))           
                # print("number: " + str(number))
        final_list.append(minimum)
        # print("final_list: " + str(final_list))
        lists[number].remove(minimum)
    return final_list

list_of_lists = [[["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"],
                  ["CS3235", "COMPUTER SECURITY", "NORMAN HUGH ANDERSON"]],
                 [["CS4221", "DATABASE DESIGN", "LING TOK WANG"],
                  ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"]]]
# print("## Q1b ##")
# print(merge(list_of_lists, module_prof))
# [[???CS1010S???, ???PROGRAMMING METHODOLOGY???, ???LEONG WING LUP, BEN???],
#  [???CS4221???, ???DATABASE DESIGN???, ???LING TOK WANG???],
#  [???CS3235???, ???COMPUTER SECURITY???, ???NORMAN HUGH ANDERSON???],
#  [???CS2010???, ???DATA STRUCTURES & ALGORITHMS II???, ???STEVEN HALIM???]

##########
# Task 2 #
##########

from math import *

def merge_sort(lst, k, field):
    
    len_list = len(lst) 
    split_list = []
    
    low = 0
    high = ceil(len_list / k)
    
    if len(lst) < 2:
        return lst
    
    for i in range(k):
        split_list += [merge_sort(lst[low:high], k, field)]
        low += ceil(len_list / k)
        high += ceil(len_list / k)
    return merge(split_list, field)

# For your own debugging
# modules = read_json('modules_small.txt')
# for module in merge_sort(modules, 2, module_code):
#    print(module)

abc = [["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"], 
       ["CS3241", "COMPUTER GRAPHICS", "CHENG HOLUN"], 
       ["CS4243", "COMPUTER VISION AND PATTERN RECOGNITION", "NG TECK KHIM"], 
       ["CS4345", "GENERAL PURPOSE COMPUTATION ON GPU", "LOW KOK LIM"], 
       ["CS3235", "COMPUTER SECURITY", "NORMAN HUGH ANDERSON"], 
       ["BT1101", "INTRODUCTION TO BUSINESS ANALYTICS", "KIM SEUNG HYUN"], 
       ["MA1101R", "LINEAR ALGEBRA I", "NG KAH LOON"], 
       ["CS3230", "DESIGN AND ANALYSIS OF ALGORITHMS", "RAHUL JAIN"], 
       ["MA1100", "FUNDAMENTAL CONCEPTS OF MATHEMATICS", "VICTOR TAN"], 
       ["ST2334", "PROBABILITY AND STATISTICS", "JASRA, AJAY"], 
       ["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"], 
       ["CS3244", "MACHINE LEARNING", "TAN CHEW LIM"], 
       ["CS5321", "NETWORK SECURITY AND MANAGEMENT", "CHANG EE-CHIEN"], 
       ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"]]

merge_sort(abc, 5, module_name)

########### DO NOT REMOVE THE TEST BELOW ###########

def print_list_to_str(list):
    return '\n'.join(str(x) for x in list)

def test(testfile_prefix):
    print("\n*** Testing with ",testfile_prefix,".txt ***")
    modules = read_json(testfile_prefix+'.txt')
    total_time = 0

    # Open correct answers
    modules_sorted_code = open(testfile_prefix+'_sorted_code.txt', 'r', encoding='utf-8').read()
    modules_sorted_name = open(testfile_prefix+'_sorted_name.txt', 'r', encoding='utf-8').read()
    modules_sorted_prof = open(testfile_prefix+'_sorted_prof.txt', 'r', encoding='utf-8').read()

    ks = [2,3,5,8,13,21,34,55,89,144]
    pass_k = 0

    for k in ks:
        start_time = time.time()
        # Execute
        modules_answer_code = merge_sort(modules, k, module_code)
        modules_answer_name = merge_sort(modules, k, module_name)
        modules_answer_prof = merge_sort(modules, k, module_prof)
        end_time = time.time()
        total_time += (end_time - start_time)

        # Check
        code_same = print_list_to_str(modules_answer_code) == modules_sorted_code
        name_same = print_list_to_str(modules_answer_name) == modules_sorted_name
        prof_same = print_list_to_str(modules_answer_prof) == modules_sorted_prof
        if (code_same and name_same and prof_same):
            pass_k += 1
        print("k = ", k, ", code: ",code_same,", name: ", name_same,", prof: ",prof_same)

    print(pass_k,"/", len(ks), " correct! Total time taken: ", total_time, " seconds.")

# print("## Q2 ##")
# test('modules_small')
# test('modules')
# test('modules_empty')