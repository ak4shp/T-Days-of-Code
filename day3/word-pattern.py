#!/usr/bin/env python3

# LEETCODE  #290 Word Pattern

'''
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
'''


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1 = {}
        d2 = {}
        p = pattern
        k = s.split()  # split sentence into list of words
        n = len(p)
        
        # edge Case :
        if len(k) != n:
            return False
        
        # storing char and words as key : value interchangeably
        for i in range(n):
            ch = p[i]
            x = d1.get(ch, False)
            if not x:
                d1[ch] = k[i]
                
            ch = k[i]
            x = d2.get(ch, False)
            if not x:
                d2[ch] = p[i]
        
        # comparing if pattern and s can be formed from each other 
        for i in range(n):
            ch = p[i]
            tch = k[i]
            if k[i] != d1[ch] or p[i] != d2[tch]:
                return False
                        
        return True