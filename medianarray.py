n=int(input())
x=list(map(int,input().split()))
n=len(x)//2
x.sort()
print(x[n])