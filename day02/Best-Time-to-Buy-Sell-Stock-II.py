#!/usr/bin/env python3

# LEETCODE  #122 Best Time to Buy and Sell Stock II
'''
Input: prices = [7,1,5,3,6,4]
Output: 7

Input: prices = [7,6,4,3,1]
Output: 0

Input: prices = [1,2,3,4,5]
Output: 4
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_day = 0
        sell_day = 1
        mxProfit = 0
        total_profit = 0
      
        for i in range(1, len(prices)):
            flag = False
            buy_pr = prices[buy_day]
            sell_pr = prices[sell_day]
            profit = sell_pr - buy_pr
      
            if prices[i] < prices[i - 1]:
                flag = True
                buy_day = sell_day
                sell_day += 1
            else:
                sell_day += 1
         
            if profit > mxProfit:
                mxProfit = profit
                    
            if flag or ((i + 1) == len(prices)):
                total_profit += mxProfit
                mxProfit = 0
          
        return total_profit
            