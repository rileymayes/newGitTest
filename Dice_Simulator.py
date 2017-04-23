# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 12:18:13 2017

@author: rlmay
"""
import random

while True:
        print random.randint(1,6)
        var = raw_input("Would you like to play again: ")
        print "You entered:", var
        if var == "yes" or var == "Yes":
            print "We'll play again!"
        else:
            print "We'll stop playing."
            break