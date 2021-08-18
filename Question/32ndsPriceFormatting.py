#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

class ThirtySecondsFormatter():
    def __init__(self, price):
        self.price = price
    
    def formatter(self):
        if(self.price > 0): #Allow for negative doubles to be formatted
            dollar = str(int(self.price)).zfill(2) #Returns the integer portion of price, with leading zeros
        else:
            dollar = "-"+str(abs(int(self.price))).zfill(2)
        fraction = str(int(32*(abs(self.price) % 1))).zfill(2) #32nd fraction of a dollar, with leading zeros
        formattedString = ("{dollar}-{fraction}").format(dollar = dollar, fraction = fraction)
        return formattedString
    

class testThirtySecondsFormatter(unittest.TestCase):
    #No rounding issues are considered
    def setUp(self):
        self.price1 = ThirtySecondsFormatter(105.37500) #Tests > 2 digit price
        self.price2 = ThirtySecondsFormatter(9.03125) #Tests leading zeros
        self.price3 = ThirtySecondsFormatter(-9.03125) #Tests negative numbers
        self.price4 = ThirtySecondsFormatter("Test") #Tests for type error if given a string input
        
    def test_formatter(self):
        self.assertEqual(self.price1.formatter(), "105-12")
        self.assertEqual(self.price2.formatter(), "09-01")
        self.assertEqual(self.price3.formatter(), "-09-01")
        
        with self.assertRaises(TypeError):
            self.price4.formatter(self.price4.formatter()) 

if __name__ == '__main__':
    unittest.main()