#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:11:35 2020

@author: rezaulkarim
"""
# Notes: in python there is a hidden variable "__name__" which is assigned
# when run directly
#if __name__ == "__main__"
#   myfunc()

# one.py

def func():
    print ('Func() in one.py')
    
print ("Top level in one.py") # Usually people assign multiple functions

if __name__ == '__main__':
    print ("One.py is bing run directly")
else:
    print ("One.py has been imported")
    
    # Usually people RUN the script after if statement
    #func()
    #func()
    # this is very common especially in modules and packages running
    