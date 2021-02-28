#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:11:59 2020

@author: rezaulkarim
"""

# two.py

import one

print ("TOP LEVEL IN TWO.PY")

one.func()

if __name__ ==  '__main__':
    print ("TWO.PY is being run directly")
    
else:
    print ("TWO.PY has been imported")