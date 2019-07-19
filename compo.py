ab=int(input())
if ab>1:
    for i in range(2,ab):
        if(ab%i)==0:
            print("yes")
            break
    else:
        print("no")
