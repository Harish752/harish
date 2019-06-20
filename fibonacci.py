num=int(input())
x=0
y=1
while(num>0):
 print(y,end=' ')
 x,y=y,x+y
 num-=1