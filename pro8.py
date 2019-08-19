def po(z,n,m):
    xy=int(n)-1
    d=int(m)-1
    mi = 0
    x = max(int(z[xy]), int(z[d]))
    for i in range(1, x + 1):
        if int(z[xy]) % i == 0 and int(z[d]) % i == 0:
            mi = i
    print(mi)

n,m=map(int,input().split())
z=list(map(int,input().split()))
p=[]
for i in range(0,m):
    xy=(input())
    p.append(xy)
for i in range(0,m):
    if len(p[i])==1:
        print(p[i])
    else:
        po(z,(p[i][0]),(p[i][2]))
