ab=int(input())
for i in range(2,ab):
    if ab%i==0:
        print("no")
        break
else:
    print("yes")