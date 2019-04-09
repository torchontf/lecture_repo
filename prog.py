import random

def num_vowels(string):
    vowels = 'aeiou'
    counter = 0
    for char in string:
        if char in vowels:
            counter = counter + 1
    return counter
