def draw(n):
    for i in range(1,n+1):
        print(" ", end="")
        for j in range(1, 2*n):
            if i == j:
                print("*"*i, end= " ")
            else:
                print(" ",end="")
        print()

    for i in range(n-1, -1, -1):
        print(" ", end="")
        for j in range( 2*n -1, -1, -1):
            if i == 0:
                continue
            if j == 2*n - i:
                print("*"*i, end= " ")
            else:
                print(" ", end='')
        print()

    


def printArrowPattern(n):
	draw(n)
	return []

s = printArrowPattern(5)
for i in s:
    print(i)
    
 
 
 #   Output -->
'''
 *         
  **        
   ***       
    ****      
     *****     
    ****       
   ***        
  **         
 *          
'''



