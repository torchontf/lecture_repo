import random

def num_vowels(string):
    vowels = 'aeiou'
    counter = 0
    for char in string:
        if char in vowels:
            counter = counter + 1
    if counter > 2:
        return True
    else:
        return False

# test statement
# print(num_vowels("yurt"))
# print(num_vowels("origami"))
