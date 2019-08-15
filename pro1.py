def high(max,l):
    xy=[]
    for i in range(0,min(len(max),len(l))):
        if max[i]==l[i]:
            xy.append(l[i])
        else: break
    return xy
n=int(input())
l=[]
for i in range(0,n):
    s=input()
    l.append(s)
max=[]
max=l[0]
for i in range(1,n):
    max=high(max,l[i])
for i in range(0,len(max)):
    print(max[i],end="")
