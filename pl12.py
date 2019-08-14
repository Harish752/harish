n,k=map(int,input().split())
xy=[]
l=list(map(int,input().split()))
xy=(l[-k:]+l[:-k])
for i in range(0,len(xy)):
	print(xy[i],end=" ")
