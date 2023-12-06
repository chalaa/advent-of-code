ans = 0
with open("input.txt","r") as lines:
    for line in lines:
        mp = {"red":0,"green":0,"blue" :0}
        ind,sts = line.split(":")
        sts = sts.split(";")
        res = 1
        for i in sts:
            i = i.strip()
            temp = i.split(",")
            r,g,b = 0,0,0
            for j in temp:
                j = j.strip()
                x,y = j.split()
                if y == "red":
                    r+=int(x)
                elif y == "blue":
                    b+=int(x)
                elif y == "green":
                    g+=int(x)
            for k in mp:
                if k == "red" and r>mp[k]:
                    mp[k] = r
                if k == "blue"and b>mp[k]:
                    mp[k] = b
                if k == "green" and g>mp[k]:
                    mp[k] = g
        for v in mp.values():
            if v>0:
                res *= v
        ans += res
print(ans)