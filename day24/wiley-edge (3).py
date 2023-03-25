s1 = input().lower()
s2 = input().lower()

mn = 0
mx = 0
for i in range(len(s1)):
    a = s1[i]
    b = s2[i]

    if a != b or (a=="?" and b=="?"):
        mx +=1

    if a != b:
        if (a=="?" or b=="?"): 
            pass
        else:
            mn += 1

print(mn, mx)



