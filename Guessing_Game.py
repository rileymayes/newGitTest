# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 17:06:25 2017

@author: rlmay
"""
import random

while True:
    num = random.randint(1,6)
    var = raw_input("Would you like to guess a number: ")
    print "You entered: ", var, "Let's check!"
    try: 
        val = int(var)
    except ValueError:
        "That's not an integer!"
    if var == num:
        print "You answered correctly!"
        var2 = raw_input("Would you like to play again: ")
        if var2 == "Yes" or var2 == "yes":
            print "We'll play again!"
        else:
            break
    elif var < num:
        print "Your guess is too low!"
        var =  raw_input("Guess again: ")
    