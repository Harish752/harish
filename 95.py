p,t,r=map(float,input().split())
r1=r/100
x=p*(1+(t*r1))
o=abs(p-x)
print(int(o))
