#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 12:10:45 2021

Password Generator Project

@author: jesus
"""

import random

nr_letters = 15
nr_symbols = 5
nr_numbers = 10

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))



# Lazy Level
password = ""

for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)
  
print( password )

# Mixing Process
password = ''.join( random.sample( password, len( password ) ) )

print( password )





