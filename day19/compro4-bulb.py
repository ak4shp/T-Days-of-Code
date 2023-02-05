s = input()

hm = {}
for i in s:
    if i not in hm.keys():
        hm[i] = 1
    else:
        hm[i] += 1

res = "Bulbasaur"
ct = 0
while True:
    i = 0
    for ch in res:
        tm = hm.get(ch)
        if tm == 0 or tm == None:
            break
        i += 1
        hm[ch] -= 1

    if i == 9:
        ct += 1

    run = hm.get("B")
    if run == 0 or run == None:
        break  

print(ct)


