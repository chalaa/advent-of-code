ans = 0
with open("input.txt","r") as lines:
    for line in lines:
        res =0
        cards = line.split(":")[-1]
        x,y = cards.split("|")
        all_num = [int(i) for i in y.split()]
        win_num = [int(i) for i in x.split()]
        for i in win_num:
            if i in all_num:
                if res == 0:
                    res = 1
                else:
                    res*=2
                ind = all_num.index(i)
                all_num[ind] = -1
        ans+=res
print(ans)