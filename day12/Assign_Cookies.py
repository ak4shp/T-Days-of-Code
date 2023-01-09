#!/usr/bin/env python3

# LEETCODE  #455. Assign Cookies
# https://leetcode.com/problems/assign-cookies/

'''
Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
'''

# Solution
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # Two pointer
        n, i, j= 0, 0, 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                n += 1
                i += 1
                j +=1 
            else:
                j += 1
        return n
        
        
        
        # Brute Force 
        '''n = 0
        g.sort()                     # nlog(n)
        s.sort()                     # mlog(m)
        for i in range(len(g)):      # n*m
            for j in range(len(s)):
                if s[j] >= g[i]:
                    s[j] = 0
                    n += 1
                    break
            

        return n'''

