o=input()
x=0
for i in range(0,len(o)-1):
    for j in range(i+1,len(o)):
        if o[i]==o[j]:
            x=x+1
if x==0:
    print("Yes")
else: print("No")
