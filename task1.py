n=int(input())
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n+1):
    for j in range(n-i):
        print(" ",end="")
    print(s[:i][::-1])
for k in range(n-1,0,-1):
    for l in range(0,n-k):
        print(" ",end="")
    print(s[:k][::-1] )