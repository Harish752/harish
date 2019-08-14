p=input()
i=0
print(p[i].upper(),end="")
i=1
while i <len(p):
    if p[i]==" ":
        print(p[i],end="")
        i=i+1
        print(p[i].upper(),end="")
        i=i+1
    else:
        print(p[i],end="")
        i=i+1
