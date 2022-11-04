#!/usr/bin/env python3

# LEETCODE  #1160 Find Words That Can Be Formed by Characters


'''
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
'''

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        dch = {}
        ans = 0 
        for i in chars:
            x = dch.get(i, False)
            if x:
                dch[i] += 1
            else:
                dch[i] = 1
                     
        for ch in words:
            dw = {}
            for i in ch:
                x = dw.get(i, False)
                if x:
                    dw[i] += 1
                else:
                    dw[i] = 1
                    
            ct = 0
            for wd, x in dw.items():
                y = dch.get(wd, False)
                
                if y:
                    if x <= y:
                        ct += x
                    else:
                        break
                        
                if ct == len(ch):
                    ans += len(ch)
                    
        return ans
            