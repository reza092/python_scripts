#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 23:48:30 2020

@author: rezaulkarim
"""
import unittest # import unittest
import Unittest_cap # import script

class TestCap(unittest.TestCase): # Create  a class that will 
                                # inherit the TestCase from unittest
    def test_one_word(self):
        text = 'python'
        result = Unittest_cap.cap_text(text) # call whatever function/class you wanna test,
                                            # here it's cap_text function will be tested
        self.assertEqual(result,'Python')
        # self.assertEqual means (I need the lowercase 'python' to pass through
        #via 'result = ' to get capitalization of first letter as 'Python')
        # action operated by the script
        
    def test_multiple_words(self):
        text = 'monty python'
        result = Unittest_cap.cap_text(text)
        self.assertEqual(result,'Monty python')
        
    def test_upper(self):
        text2 = 'cat'
        result2 = text2.upper()
        self.assertEqual(result2,'CAT')
        
    def test_isupper(self):
        text3 = 'dog'
        result3 = text3.upper()
        self.assertTrue(result3.isupper)
        self.assertFalse(result3.isupper)
        
    def test_split(self):
        text4 = 'barking puppy'
        result4 = text4.split()
        self.assertEqual(['barking','puppy'],result4.split)
        
if __name__ == '__main__':
    unittest.main()
    