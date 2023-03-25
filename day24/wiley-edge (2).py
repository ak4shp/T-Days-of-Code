def draw(n):
    for i in range(1,n+1):
        for j in range(1, 2*n):
            if i == j or j == 2*n - i:
                print(i, end= " ")
            else:
                print(" ",end="")
        print()

    for i in range(n-1, -1, -1):
        for j in range( 2*n -1, -1, -1):
            if i == 0:
                continue
            if i == j or j == 2*n - i:
                print(i, end= " ")
            else:
                print(" ", end='')
        print()

    
n = int(input())
draw(n)




