ans = []
with open("myfile.txt","r") as lines:
    for line in lines:
        res = []
        for i in line:
            if i.isnumeric():
                res.append(i)
        ans.append(int(res[0]+res[-1]))
print(sum(ans))