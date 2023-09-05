""" Determines Largest Number """
#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: September 2023

import random

# Finds the x biggest number in an array
def x_biggest_number(array, x_highest):
    sorted_array = []
    
    # Finds highest numbers from largest to smallest
    increment = 0
    while increment < len(array):
        current_largest_index = 0
        number = 0
        while number < len(array):
            if array[number] > array[current_largest_index]:
                current_largest_index = number
            number += 1
        sorted_array.append(array[current_largest_index])
        array[current_largest_index] = 0
        increment += 1

    print(sorted_array)
    return(sorted_array[x_highest - 1])

def main():

    # Generates random array of 10 numbers
    list_of_numbers = [random.randint(0,100), random.randint(0,100),
            random.randint(0,100), random.randint(0,100),
            random.randint(0,100), random.randint(0,100),
            random.randint(0,100), random.randint(0,100),
            random.randint(0,100), random.randint(0,100)]

    print("List of 10 numbers", list_of_numbers)
    # Makes sure the input is valid
    try:
        x_largest = int(input("which largest number would you like to guess"
                + " (1st, 2nd, 3rd, etc.)? "))
        if x_largest < 1 or x_largest > 10:
            print("please input a real number from 1-10")
        else:
            print(x_biggest_number(list_of_numbers, x_largest))
            
    except:
        print("Pleas input an actual number")

if __name__ == "__main__":
        main()
