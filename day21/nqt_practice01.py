''' Given an integer array Arr of size N
    the task is to find the count of elements whose value is greater than all of its prior elements.
    Note : 1st element of the array should be considered in the count of the result.
'''

n = int(input())
comp = float("-inf")
ct = 0
for i in range(n):
    a = int(input())
    if a >= comp:
        comp = a
        ct += 1

print(ct)