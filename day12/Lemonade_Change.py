#!/usr/bin/env python3

# LEETCODE  #860. Lemonade Change
# https://leetcode.com/problems/lemonade-change/description/

'''
Example 1:

Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:

Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.

'''

# Solution
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        fv, tn = 0, 0 
        for pay in bills:
            if pay == 5:
                fv += 1

            elif pay == 10:
                tn += 1
                if fv == 0:
                    return False 
                fv -= 1

            else:
                if tn > 0 and fv > 0:
                    tn -= 1
                    fv -= 1

                elif fv >= 3:
                    fv -= 3

                else:
                    return False

        return True
        
        
        # Scattered 
        '''fv, tn = 0, 0 
        flag = False

        for pay in bills:
            flag = True
            if pay == 5:
                fv += 1
            elif pay == 10:
                tn += 1
           
            rem = pay - 5
            if pay > 5:
                if rem == 5:
                    if fv > 0:
                        fv -= 1
                        rem = 0
                   
                if rem == 15:
                    if fv > 0:
                        if tn > 0:
                            tn -= 1
                            fv -= 1
                            rem = 0
                           
                        elif fv >= 3:
                            fv -= 3
                            rem = 0
                
            if rem != 0:
                flag = False
                break
            
        return flag'''
               
               
                    
            

            

