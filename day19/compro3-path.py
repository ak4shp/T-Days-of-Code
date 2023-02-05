n = int(input())
ro = int(input())
re = int(input())
oe = int(input())

pos = "r"
ans = 0
if n == 1:
    print(0)

else:
    n -= 1
    while n:
        n -= 1
        if pos == "r":
            if ro < re:
                pos = "o"
                ans += ro
            else:
                pos = "e"
                ans += re

        elif pos == "o":
            if ro < oe:
                pos = "r"
                ans += ro
            else:
                pos = "e"
                ans += oe

        else:
            if re < oe:
                pos = "r"
                ans += re
            else:
                pos = "o"
                ans += oe
    print(ans)
