xy=list(map(str,input()))
t=""
for i in range(0,len(xy)-1,2):
    t=xy[i]
    xy[i]=xy[i+1]
    xy[i+1]=t
for i in range(0,len(xy):
    print(xy[i],end="")
