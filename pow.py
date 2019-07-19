n,m=map(int,input().split())
a=n*m
for i in range(0,a+1):
    if(i**2==a):
        print("yes")
        break
else:
    print("no")
    
