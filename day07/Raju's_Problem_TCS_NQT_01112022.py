# TCS NQT 01-11-2022 1:30PM

"""
Raju's computer teacher is a funny person. His problems are more focused on mathematics rather than computer programming. given questions are always with a twist. This time he has gave a question on arrays, but it had a flavor of linear equations.
Below is question for which you have to write a program.
 
• You have been given an N-sized array, which starts from index 1
• Initially, all the elements in the array are 0.
• There will be Q update queries by the user (in the form of X and Y). For each query, there will be an increment of Value of 1, for each index.
• The index will be decided as per the equation index =  X*C+Y, where X and Y will be positive integers given by the user and C is a counter ranging from 0 to infinity 

At the end of Q queries, you have to find the final array

INPUT -->
3 1  -> N Q 
1 3  -> Qth Query

OOUTPUT -->
0 0 1

INPUT -->
7 4  -> N Q 
1 3  -> Qth Query
7 7  -> Qth Query
7 3  -> Qth Query
2 2  -> Qth Query

OOUTPUT -->
0 1 2 2 1 2 2
"""


def solve(N, Q, queries):
    arr = [0]*N 
    for qr in queries:
        x = qr[0]
        y = qr[1]
        c = 0
        while True:
            idx = x * c + y
            if idx > N:
                break
            arr[idx-1] = arr[idx-1] + 1
            c += 1
            
    return arr
    
# Testing main
print(solve(3, 1, [[1, 3]]))
print(solve(7, 4, [[1, 3], [7, 7], [7, 3], [2, 2]]))
print(solve(2000, 20, [[1, 3], [7, 78], [7, 3], [2, 2], [2, 1], [1, 3], [7, 7], [7, 3], [2, 2], [2, 1], [1, 3], [7, 78], [7, 3], [2, 2], [2, 1], [1, 3], [7, 7], [7, 3], [2, 2], [2, 1]]))