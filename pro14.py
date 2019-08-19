n,k=map(int,input().split())
xyz=list(map(int,input().split()))
q=[]
for i in range(0,k):
    d = []
    d=list(map(int,input().split()))
    s = xyz[d[0]-1]
    for j in range(min(d),max(d)):
        s=s^xyz[j]
    q.append(s)
for i in range(0,len(q)):
    print(q[i])
