n=list(map(str,input()))
p=""
for i in range(0,len(n)-1,2):
    t=n[i]
    n[i]=n[i+1]
    n[i+1]=p
for i in range(0,len(n)):
    print(n[i],end="")
