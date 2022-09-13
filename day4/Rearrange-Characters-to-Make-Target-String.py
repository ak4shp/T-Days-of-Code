#!/usr/bin/env python3

# LEETCODE  #2287. Rearrange Characters to Make Target Stringy


'''
Input: s = "abcba", target = "abc"
Output: 1

Input: s = "abbaccaddaeea", target = "aaaaa"
Output: 1

Input: s = "ilovecodingonleetcode", target = "code"
Output: 2
'''

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d1 = {}
        d2 = {}
        
        for i in s:
            x = d1.get(i, False)
            if x:
                d1[i] += 1
            else:
                d1[i] = 1
        
        for i in target:
            x = d2.get(i, False)
            if x:
                d2[i] += 1
            else:
                d2[i] = 1
                
        res = 100          # 1 <= s.length <= 100
        for k, v in d2.items():
            x = d1.get(k, False)
            if x:
                rs = x // v
                res = min(rs, res)
            else:
                return 0
            
        return res 
        
        