#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 03:42:17 2020

@author: rezaulkarim
"""
# try .. except is a good means to capture errors in code

# try:
#     # WANT TO ATTEMPT THIS BLOCK OF CODE
#     # MAY PRODUCE ERROR
#     RESULT = 10 + '10'
# except:
#     # IF THE TRY SECTION PRODUCES ERROR THIS BLOCK WILL RUN
#     print('It looks like addition failed!')
    
# error handling during file open/writing

# try:
#     #f = open('testfile','w')
#     f = open('testfile','r')
#     #f.write('Write a test line')
#     f.read()
# except TypeError:
#     # many types can be captured
#     print('It has type errr')
# # except OSError:
# #     print('You have an OS error')
# except:
#     print('All other errors') # in large script, mostly it will be try except finally
# finally:
#     print("I always run")
    
# How to use try except finally block in functions
def ask_for_int():
    while True:
        try:
            result = int(input("please provide a number: "))
        except:
            print("Whops! That is not a number")
            continue
        else:
            print("yes, thank you")
            break
        # finally:
        #     print("I am going to ask you again! \n")
            
ask_for_int()