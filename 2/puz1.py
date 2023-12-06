dic = {
    "red":12,
    "green":13,
    "blue" :14
}
ans = 0
with open("input.txt","r") as lines:
    for line in lines:
        ind,sts = line.split(":")
        ind = ind.split()[-1]
        sts = sts.split(";")
        for i in sts:
            i = i.strip()
            flag = True
            mp = {"red":0,"green":0,"blue" :0}
            for j in i.split(","):
                j = j.strip()
                x,y = j.split()
                mp[y] += int(x)
            
            for k in dic:
                if mp[k] > dic[k]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            ans += int(ind)
print(ans)