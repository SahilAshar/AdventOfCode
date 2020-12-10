import csv

input_list = []

# convert text file into list
input_file = open("input.txt")
file_contents = input_file.read()
input_list = file_contents.splitlines()
input_list = list(map(int, input_list)) 

####################
# Part 1

# sort list
input_list.sort()

# two pointer method to find sum of 2020
sum = 0
fp = 0
lp = len(input_list) - 1

while sum != 2020:
    sum = input_list[fp] + input_list[lp]
    if sum > 2020:
        lp -= 1
    elif sum < 2020:
        fp += 1

# print(input_list)

print(
    str(fp) + " : " + str(input_list[fp]) + 
    " | " + str(lp) + " : " + str(input_list[lp]) + 
    " | " + str(input_list[fp] + input_list[lp]) + 
    " | " + str(input_list[fp] * input_list[lp])
    )

####################
# Part 2

sum = 0
fp = 0
lp = len(input_list) - 1
mp = int(lp/2)

while sum != 2020:
    sum = input_list[fp] + input_list[mp] + input_list[lp]
    print(str(sum) + " | " + str(input_list[fp]) + " " + str(input_list[mp]) + " " + str(input_list[lp]))
    if sum > 2020:
        lp -= 1
    elif sum < 2020:
        fp += 1
        mp += 1

print(
    str(fp) + " : " + str(input_list[fp]) + 
    " | " + str(mp) + " : " + str(input_list[mp]) +
    " | " + str(lp) + " : " + str(input_list[lp]) + 
    " | " + str(input_list[fp] + input_list[lp] + input_list[lp]) + 
    " | " + str(input_list[fp] * input_list[mp] * input_list[lp])
    )