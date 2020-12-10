import csv
import itertools

# Brute Force Solutions

input_list = []

# convert text file into list
input_file = open("input.txt")
file_contents = input_file.read()
input_list = file_contents.splitlines()
input_list = list(map(int, input_list)) 


def prod(val) :  
    res = 1 
    for ele in val:  
        res *= ele  
    return res 

def get_tuple_product(num):
    for result in itertools.combinations(input_list, num):
        tuple_sum = sum(list(result))
        if tuple_sum == 2020:
            return prod(result)

####################
# Part 1
print(get_tuple_product(2))

####################
# Part 2
print(get_tuple_product(3))
