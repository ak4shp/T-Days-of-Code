#!/usr/bin/env python3

# LEETCODE  #205 Isomorphic Strings
'''
Input: s = "paper", t = "title"
Output: true

Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "badc", t = "baba"
Output: false
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        n = len(s)
        
        for i in range(n):
            ch = s[i]
            x = d1.get(ch, False)
            if not x:
                d1[ch] = t[i]
                
            ch = t[i]
            x = d2.get(ch, False)
            if not x:
                d2[ch] = s[i]

        for i in range(n):
            ch = s[i]
            tch = t[i]
            if t[i] != d1[ch] or s[i] != d2[tch]:
                return False
                        
        return True
                
                