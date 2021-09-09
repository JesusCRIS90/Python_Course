#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:52:42 2021

Ejemplo de Manipulacion de f-String

@author: jesus
"""

import random
from replicant import clear
import turtle

# Day 2 - Important knowledge
var1 = 0
var2 = 12.4
var3 = False

# Uso de f-String

f_string1 = f"Var 1: { var1 }, Var 2: { var2 }, Var 3: { var3 }"

# Day 4 - Important knowledge

print( random.choice( [ "A", "B", "C", "D", "E", "F", "G", "H" ] ) )


# Day 5
"""
If we set the value for argument in the definition of the function, when we use
that function we can use the keyword to making a reference in the argument 
""" 
def do_somthing_fun( A = 2, D = "P", C = 7 ):
    """
        Write here what the function do
    """
    # Do something
    return

do_somthing_fun()                       # Use default values
do_somthing_fun( 1, "A", 0 )            # Use custom values using position arguments
do_somthing_fun( b ="A",  c = 1 )       # Use custom values using keyword arguments


# Day 9

empty_dictionary = {}
empty_dictionary["Data_1"] = 1029       # Adding element to dictionary
print( empty_dictionary["Data_1"] )     # Making a query to the dictionary

"""
    To  clear de console use the module replicant
    from replicant import clear
"""

# Day 10

"""
    Assign a function to a variable. Running that function using the variable.
"""

def func1():
    print("func1")

def func2():
    print("func2")
    
def func3():
    print("func3")
    
def func4():
    print("func4")

func_dict = { 1: func1, 2: func2, 3: func3, 4: func4 }

f = func_dict[1]
f()




myScreen = turtle.Screen()
myScreen.exitonclick()




