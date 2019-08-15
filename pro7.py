xy=int(input())
m=1000
for i in range(0,20):
    if pow(2,i)<=xy:
        x = abs(pow(2, i) - xy)
        if x < m: m = x
print(m)
