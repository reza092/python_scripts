#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 18:30:56 2020

@author: rezaulkarim
"""

## Write a function that return True if 007 is in the list
def spy_game(nums):
    
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
            
    return len(code) == 1

print(spy_game([0,0,5,0,7]))

## Write a function that returns the number of prime numbers that exist upto
# including a given number
def count_primes(num):
    
    if num < 2:
        return 0
    
    primes = [2]
    x = 3
    
    while x <= num:
        for y in range(3,x,2):
            if x %y == 0:
                x += 2
                break
            
        else:
            primes.append(x)
            x += 2
            
    print (primes)
    return len(primes)

## Write a function that takes a single letter, and returns a 5X5 representation
    # of that letter
def print_big(letter):
    patterns = {
        3: '  *  ', 24: ' * * ', 15: '*   *', 40: '**** ', 50: '*****', 4: '   * ',
        5: '    *', 2: ' *   ', 1: '*    ', 30: '***  ', 23: ' **  ', 25: ' *  *',
        34: '  ** ', 14: '*  * '
        }
    alphabet = {'A':[3,24,50,15,15], 'B':[30,15,30,15,30], 'C':[34,25,1,25,34], 
                'D':[30,14,15,14,30], 'T':[50,3,3,3,3]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
    