m,n=map(int,input().split())
x=0
for p in range(m,n+1):
    if p == 2 or p == 3 or p == 5 or p == 7:
        x=x+1
    elif (p % 2 != 0) and (p % 3 != 0) and (p % 5 != 0) and (p % 7 != 0) and (p != 1) and p > 0:
        x=x+1
print(x) 
