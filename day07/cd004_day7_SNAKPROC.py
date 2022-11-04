#!/usr/bin/env python3

# Codechef --> SNAKPROC
# https://www.codechef.com/submit/SNAKPROC

'''
INPUT ->
6
18
..H..T...HTH....T.
3
...
10
H..H..T..T
2
HT
11
.T...H..H.T
7
H..T..H

OUTPUT ->
Valid
Valid
Invalid
Valid
Invalid
Invalid
'''


def is_valid(snake):
    new_snake = snake.replace(".", "")
    del_HT_snake = new_snake.replace("HT", "")
    
    if len(del_HT_snake) == 0:
        return "Valid"
        
    return "Invalid"
    
    
for _ in range(int(input())):
    
    n = int(input())
    snake = input()
    print(is_valid(snake))
    