import csv

# Brute Force Solution

input_file = open("input.txt")
file_contents = input_file.read()
input_list = file_contents.splitlines()

def parse(password_item):
    parsed_pw = password_item.split(" ")
    parsed_pw[0] = list(map(int, parsed_pw[0].split("-")))
    parsed_pw[1] = parsed_pw[1][:-1]
    parsed_pw[2] = create_password_map(parsed_pw[2])
    
    #print(parsed_pw)
    return parsed_pw
    
def create_password_map(password_str):
    return { char:(password_str.count(char)) for char in password_str }

def check(parsed_pw):

    pw_char_count = parsed_pw[2].get(parsed_pw[1])

    if pw_char_count is None:
        return False  

    if (pw_char_count >= parsed_pw[0][0]) and (pw_char_count <= parsed_pw[0][1]):
        return True

    return False

def count_valid_passwords(): 
    total = 0
    for password in input_list: 
        parsed_pw = parse(password)
        if check(parsed_pw) is True:
            total += 1

    return total


####################
# Part 1
print(count_valid_passwords())
