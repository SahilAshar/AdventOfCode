import csv
from operator import xor

# Brute Force Solution

input_file = open("input.txt")
file_contents = input_file.read()
input_list = file_contents.splitlines()

def parse(password_item):
    parsed_pw = password_item.split(" ")
    parsed_pw[0] = list(map(int, parsed_pw[0].split("-")))
    parsed_pw[1] = parsed_pw[1][:-1]
    
    return parsed_pw

def check(parsed_pw):

    f_idx = parsed_pw[0][0] - 1
    l_idx = parsed_pw[0][1] - 1

    return xor(parsed_pw[1] == parsed_pw[2][f_idx], parsed_pw[1] == parsed_pw[2][l_idx])

def count_valid_passwords(): 
    total = 0
    for password in input_list: 
        parsed_pw = parse(password)
        if check(parsed_pw) is True:
            total += 1

    return total


####################
# Part 2
print(count_valid_passwords())
