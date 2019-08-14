xy=int(input())
f=1
i=0
for i in range(xy,0,-1):
    f=f*i
if xy==0:
    print("1")
else:
    print(f)
