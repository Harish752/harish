xyz=int(input())
s=0
m=list(map(int,input().split()))
for i in range(0,xyz-1):
    for j in range(0,xyz):
        if m[i]<m[j]:
            s=s+(i+1)
print(s)
