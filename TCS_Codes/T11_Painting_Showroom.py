class Painting:
    def __init__(self, id, name, price, typ):
        self.id = id
        self.name = name
        self.price = price
        self.typ = typ


class ShowRoom:
    def __init__(self, plist):
        self.plist = plist

    def get_total_price(self, query):
        total = 0
        f = 0
        for p in self.plist:
            if p.typ.lower() == query.lower():
                f = 1
                total += p.price
        if f == 1:
            return total
        else:
            return None
        
    def get_max_painter(self):
        pcount = {}
        for p in self.plist:
            if p.name not in pcount.keys():
                pcount[p.name] = 1
            else:
                pcount[p.name] += 1

        d = dict(sorted(pcount.items(), key=lambda x:x[1], reverse=True))
        # print(d)
        # d = sorted(d.items(), key=lambda x:x[0], reverse=False)
        mx = max(d.values())
        # print(mx)
        # ans = d.get(mx)
        # print(ans)
        ans = []
        for k, v in d.items():
            if v < mx:
                break
            ans.append([k, v])

        # print("aa", ans)
        ans = sorted(ans, key=lambda x : x[0], reverse=False)
        # print(d2)
        return ans[0][0]


n = int(input())
plist = []
for i in range(n):
    id = input()
    name = input()
    price = int(input())
    typ = input()

    paint = Painting(id, name, price, typ)
    plist.append(paint)

query = input()

show = ShowRoom(plist)

total = show.get_total_price(query)
print(total if total is not None else "No paiting found")
painter = show.get_max_painter()
print(painter)

