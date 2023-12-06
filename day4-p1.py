import pandas as pd
import numpy as np 

with open(r'C:\Users\Gabriel Marinho\OneDrive\Área de Trabalho\fun\AoC\cards.txt', 'r') as file:

    first_10_digits = []
    remaining_digits = []

    for line in file:
        line = line.strip()
        first_10 = line[10:40]
        first_10_digits.append(first_10)
        remaining = line[41:]
        remaining_digits.append(remaining)


def separate_characters(string):
    numbers = string.split()
    return numbers

temp_array = []
temp_array2 = []
cards_worth = np.zeros(len(first_10_digits))

for i in range(len(first_10_digits)):
    is_first_match = True
    temp_array = separate_characters(first_10_digits[i])
    temp_array2 = separate_characters(remaining_digits[i])
    for x in range(len(temp_array)):
        for y in range(len(temp_array2)):
            if temp_array[x] == temp_array2[y]:
                if is_first_match == True:
                    cards_worth[i] = 1           
                else:
                    cards_worth[i] = 2*cards_worth[i]
                is_first_match = False

cards_worth_sum = np.sum(cards_worth)
print(cards_worth_sum)

                

