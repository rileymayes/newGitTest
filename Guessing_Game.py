# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 17:06:25 2017

@author: rlmay
"""
import random

def valid_number(s):
    if s.isdigit() and 1 <= int(s) <= 3
        return True
    else:
        return False

def main():
    num = random.randint(1,3)
    number_guesses = 0
    var = raw_input("Would you like to guess a number: ")
    print "You entered: ", var, "Let's check!"
    while not False:
        if not valid_number(guess):
            guess = raw_input("That isn't a number. Please pick a number: ")
            continue
        else:
            number_guesses = +=1
            guess = int(guess)
        
        if var == num:
            print "You answered correctly!"
            print "It took", number_guesses, "to get the answer."
            break
        elif var < num:
            print "Your guess is too low!"
            var =  raw_input("Guess again: ")
        elif var > num:
            print "Your guess is too high!"
            var =raw_input("Guess again: ")
