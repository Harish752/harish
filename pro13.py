n,k=map(int,input().split())
xyz=list(map(int,input().split()))
q=[]
for i in range(0,k):
    d = []
    d=list(map(int,input().split()))
    s = d[0]
    for j in range(min(d)-1,max(d)):
        if s>xyz[j]: s=xyz[j]
    q.append(s)
for i in range(0,len(q)):
    print(q[i])
