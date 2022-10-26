#!/usr/bin/env python3

# CAMPUS  #Nucleus company-> 
'''given two arrays having UniqueID and corresponding Profit, 
Find maximum profit of a pair of UniqueID in which UniqueID is different'''


'''
Input: UniqueID = [4, 6, 3, 3, 4]
       Profit= [-1, 10, 10, 15, -3]
Output: 25
Explain : ids at idx 1 and 3 (6, 3) -> (10 + 15)

'''
# CPP code ->>>
'''
#include <iostream>
using namespace std;

int main() {
    /*  U = Unique id  
        P = Profit
    */
    
    int n = 5;
    int U[5] = {4, 6, 3, 3, 4};
    int P[5] = {-1, 10, 10, 15, -3};
    
    int sm = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j ++) {
            int tmp = 0;
            if (U[i] != U[j]) {
                tmp = P[i] + P[j];
            }
            
            if (sm < tmp) {
               sm = tmp;
            }
        }
    }        
    return sm;
}
'''

# python Code ->>>

def solve(uid : list, profit : list, n : int) -> int:
    sm = 0
    for i in range(n):
        for j in range(i + 1, n):
            tmp = 0
            if (uid[i] != uid[j]):
                tmp = profit[i] + profit[j]
            if sm <= tmp:
                sm = tmp
    
    return sm

print(solve([3, 3, 3, 3, 3], [-1, 10, 10, -15, -3], 5))
