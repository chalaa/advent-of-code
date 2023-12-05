ans = []
st = {"one":'1', "two":'2', "ree":'3', "our":'4', "ive":'5', "six":'6', "ven":'7', "ght":'8',"ine":'9'}
with open("myfile.txt","r") as lines:
    for line in lines:
        res = []
        for i in range(len(line)):
            if line[i].isnumeric():
                res.append(line[i])
            elif i >= 2:
                s = line[i-2:i+1]
                if s in st:
                    res.append(st[s])
        ans.append(int(res[0]+res[-1]))
print(sum(ans))