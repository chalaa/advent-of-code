from collections import defaultdict
from queue import PriorityQueue

dic = defaultdict(int)
qe = PriorityQueue()
ans=0

with open("input.txt","r") as lines:
    for line in lines:
        res =0
        ind,cards = line.split(":")
        ind = int(ind.split()[-1])
        x,y = cards.split("|")
        all_num = [int(i) for i in y.split()]
        win_num = [int(i) for i in x.split()]
        for i in win_num:
            if i in all_num:
                res+=1
        dic[ind]= res
        for i in range(ind+1,ind+res+1):
            qe.put(i)
        ans+=1
while not qe.empty():
    top = qe.get()
    res = dic[top]
    for i in range(top+1,top+res+1):
            qe.put(i)
    ans+=1
print(ans)