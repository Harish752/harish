p,m=list(map(str,input().split()))
xy=0
if p==m: print(xy)
elif len(p)>len(m):
    p=list(p)
    m=list(m)
    for i in range(0,len(m)):
        for j in range(0,len(p)):
            if p[j]==m[i]:
                p.pop(j)
                break
    xy=len(p)
    print(xy)
else:
    for i in range(0, min(len(p), len(m))):
        if p[i] != m[i]:
            xy = xy + 1
        if i == min(len(p), len(m)) - 1:
            xy = xy + abs((i + 1) - max(len(p), len(m)))
    print(xy)
