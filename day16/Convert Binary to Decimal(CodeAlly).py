"""
Multiply the digits of given number untill the number becomes single digit.

Example 1
input : 101011
output : 43 (1*32 + 0*16 + 1*8 + 0*4 + 1*2 + 1*1)


Example 2
input : 1001
output : 9
"""

# Do NOT edit nor remove any existing code when testing or submitting
def main_function(input):
    # Place your code here
    num = int(input)
    res = 0
    pw = 0

    while num > 0:
        rem = num % 10
        num = num // 10
        res += rem * (2 ** pw)
        pw += 1

    return res


# number = input()
# print(main_function(number))
