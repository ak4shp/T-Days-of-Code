#!/usr/bin/env python3

# LEETCODE  #392 Is Subsequence
'''
Input: s = "axc", t = "ahbgdc"
Output: false

Input: s = "abc", t = "ahbgdc"
Output: true

Input: s = "", t = "ahbgdc"
Output: true
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        ct = len(s)        
        if ct == 0:
            return True
      
        for _ in range(len(t)):
            si = s[i]
            tj = t[j]
            
            if si == tj:
                i += 1
                j += 1
                ct -= 1
                
                if ct == 0:
                    return True
            else :
                j += 1

        return False
    
    