
def check(num):
    '''Dictionry to count occurrence of a digit in the number.
       Key -> (Digit) | Value -> count'''
    digit_count = {0:0, 1:0, 2:0, 3:0, 4:0, 
                   5:0, 6:0, 7:0, 8:0, 9:0}
    
    num_str = str(num)
    for ch in num_str:
        digit_count[int(ch)] += 1
    
    if max(digit_count.values()) > 1:
        return False
    return True

#* Main 
n1 = int(input("num 1= "))
n2 = int(input("num 2= "))
count = 0
unique_nums = []   #! Mitra! ye list banana sirf ans shwo krne ke liye hai.
for i in range(n1, n2+1):
    if check(i):
        count += 1
        unique_nums.append(i)

print("Ans: ", count)
print("No Repeat numbers: ", unique_nums)






