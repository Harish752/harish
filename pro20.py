n,m=map(int,input().split())
xyy=list(map(int,input().split()))
u=0
c=sorted(xyy)
x=(c[::-1])
for i in range(0,len(x)):
    a = m //(x[i])
    u = u + a
    m = m - (a *x[i])
print(u)
