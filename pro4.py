ab,cd=map(str,input().split())
s=0
if len(ab)==len(cd):
    for i in range(0,len(ab)):
        s=s+(abs(ord(ab[i])-ord(cd[i])))
else:
    for i in range(0,len(ab)):
        s=s+(abs(ord(ab[i])-ord(cd[i])))
    d=abs(len(ab)-len(cd))
    for i in range(0,d):
        s=s+ord(cd[len(ab)+i])-96
print(s)
