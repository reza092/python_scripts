# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# for i in ['a','b','c']:
#     try:
#         print(i**2)
#     except:
#         print('Wrong data type')
#         break

    
# # problem #2
        
# x = 5
# y = 0

# try:
#     z = x/y
# except:
#     print('Division error')
# finally:
#     print('All Done')
    
# Write a function that asks for an integer and prints the square of it.
#Use a while loop with a try, except, else block to account for incorrect
#inputs.

def ask():
    wait = True
    while wait:
        try:
            user = int(input('Input: '))
            
        except ValueError:
            print('Please input only the integers')
        else:
            wait = False
            
    print("Your number squared is")
    print ((user**2))