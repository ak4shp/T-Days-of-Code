# https://www.codechef.com/problems/WORDLE

t = int(input())
while t:
    ans = ""
    t -= 1 
    s = input()
    k = input()
    
    for i in range(5):
        if s[i] == k[i]:
            ans += "G"
        else:
            ans += "B"
    print(ans)
    
    