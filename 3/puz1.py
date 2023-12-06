data = []
ans = 0
st ={'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}','_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
with open("input.txt","r") as lines:
    for line in lines:
        x = list(line.strip())
        x.insert(0,'.')
        x.append('.')
        data.append(x)
data.insert(0, ['.']*len(data[0]))
data.append(['.']*len(data[0]))
for i in range(len(data)):
    j = 0
    while j < len(data[i]):
        flag = False
        temp = ""
        while j < len(data[i]) and data[i][j].isnumeric():
            temp+=data[i][j]
            if data[i-1][j-1] in st or data[i-1][j] in st or data[i-1][j+1] in st or data[i][j-1] in st or data[i][j+1] in st or data[i+1][j-1] in st or data[i+1][j] in st or data[i+1][j+1] in st:
                flag = True
            j+=1
        if flag:
            ans+=int(temp)
        j+=1
print(ans)
            