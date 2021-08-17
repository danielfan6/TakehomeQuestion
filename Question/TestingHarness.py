#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 12:48:42 2021

@author: DanielFan
"""
import unittest

def longestCommonPrefix(strs):
    firstword = strs[0]
    prefix = ""
    numberOfWords = len(strs)
    for i in range(0,len(firstword)):
        letter = firstword[i].lower()
        for word in range (0,numberOfWords):
            if((i == len(strs[word])) or (strs[word][i].lower() != letter)):
                return firstword[0:i].lower()
        
    return prefix

class testPrefix(unittest.TestCase):
    
    def test_pref(self):
        self.assertEqual(longestCommonPrefix(["flower","flow","flight"]), "fl", "Should be fl")

if __name__ == '__main__':
    unittest.main()
    
def testing():
    assert(longestCommonPrefix(["flower","flow","flight"]) == "fl")
    assert(longestCommonPrefix(["","Ad", "30"]) == "")
    assert(longestCommonPrefix(["","Ad", "Ad"]) == "")
    assert(longestCommonPrefix(["","", ""]) == "")
    assert(longestCommonPrefix(["Ad","Ad", ""]) == "")
    assert(longestCommonPrefix(["Adele","Ade", "Ade"]) == "ade")
    assert(longestCommonPrefix(["Ern","error", "eRno"]) == "er")
    
    
        
        
                   
    
    