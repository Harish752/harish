from itertools import combinations
xx,yy=map(int,input().split())
h=len(str(xx))
lv=list(combinations(str(xx),h-yy))
lv=(sorted(lv))
x="".join(lv[0])
print(x)
