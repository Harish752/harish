z=input()
n=len(z)
if n%2!=0:
    z=z[:int(n/2)]+'*'+z[int(n/2)+1:n]
else:
    z=z[:int(n/2)-1]+'**'+z[int(n/2)+1:n]
print(z)
