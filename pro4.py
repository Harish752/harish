n,k=map(str,input().split())
ab=0
if len(n)==len(k):
    for i in range(0,len(n)):
        ab=ab+(abs(ord(n[i])-ord(k[i])))
else:
    for i in range(0,len(n)):
        ab=ab+(abs(ord(n[i])-ord(k[i])))
    d=abs(len(n)-len(k))
    for i in range(0,d):
        ab=ab+ord(k[len(n)+i])-96
print(ab)
