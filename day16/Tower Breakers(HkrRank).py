#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/one-week-preparation-kit-tower-breakers-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-three


# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#





def towerBreakers(n, m):
    return (1, 2)[n % 2 == 0 or m == 1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
    
    
"""
            <<  APPROACH  >>

The task is confusing, the key here is not in to count the moves but to find an optimal moving strategy.
The only exception is (m == 1) there is no moves with any towers count so P1 loose. (you don't need m anymore)

n == 2 - optimal strategy for P2 is to copy moves. It will allow him to win no matter how big is m.

n == 3 - the winnig strategy for P1 is remove max number in one tower,
         so situation would be same as (n = 2) but with P2 moves first now. So P1 will always win. P2 can't do anything.

n == 4 - P2 has advantage again. P2 will copy until the situation is equal to (n == 2). P2 wins

n == 5 - P1 does the same trick as with (n == 3), and has reverted situation of (n == 4). P1 wins

And so on pattern repeates...

"""
