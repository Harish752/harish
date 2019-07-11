l=input()
for i in range(0,len(l)):
   if(l[i].isalpha() and l[i].isdigit()):
    print("No")
else:
  print("Yes")