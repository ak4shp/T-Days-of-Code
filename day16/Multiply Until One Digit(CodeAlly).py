"""
Multiply the digits of given number untill the number becomes single digit.

Example 1
input : 47 -> 4*7 = 28 -> 2*8 = 16 -> 1*6 = 6 (single digit)
output : 6

Example 2
input : 120
output : 0
"""


# Do NOT edit nor remove any existing code when testing or submitting
def main_function(input):
    # Place your code here
    # print("ggg")
    num = int(input)
    if num < 10:       # Recursion return condition
        return num  
    nb = num
    num = 1
    while nb > 0:
        rem = nb % 10
        nb = nb //10
        num *= rem
        # print(nb, rem, num)
    return main_function(num)  #Recursion

# number = input()
# print(main_function(number))
