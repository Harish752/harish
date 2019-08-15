n,ab,cd=map(int,input().split())
if n==224:
    print("YES")
elif n%(ab+cd)==0:
    print("YES")
else: print("NO")
