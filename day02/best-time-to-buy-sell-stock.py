#!/usr/bin/env python3

# LEETCODE  #121 Best Time to Buy and Sell Stock
'''
Input: prices = [7,1,5,3,6,4]
Output: 5

Input: prices = [7,6,4,3,1]
Output: 0
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_day = 0
        sell_day = 1
        mxProfit = 0
        
        for i in range(1, len(prices)):
            buy_pr = prices[buy_day]
            sell_pr = prices[sell_day]
            profit = sell_pr - buy_pr
           
            if profit < 0:
                buy_day = sell_day
                sell_day += 1
            else:
                sell_day += 1

            if profit > mxProfit:
                mxProfit = profit
            
        return mxProfit
            