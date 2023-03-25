s = input()
sz = len(s)

if s[-1].isdigit():
    ln = sz-1
    new = s[:-2]+str(ln)
    if new[-2:len(new)] == str(ln):
        print(str(ln)[1])
    else:
        print(-1)

else:
    print(sz if sz<=9 else -1)


