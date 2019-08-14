nn=list(map(str,input()))
tt=""
for i in range(0,len(nn)-1,2):
    tt=nn[i]
    nn[i]=nn[i+1]
    nn[i+1]=tt
for i in range(0,len(nn)):
    print(nn[i],end="")
