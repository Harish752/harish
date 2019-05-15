print ("enter the values of a &b")

a=str(input())

b=str(input())

if a.isalpha() or b.isalpha():

	print("is a alphabet")

print("enter the operator choice")

ch=int(input())

if ch == 1:
   
	print(a+b)

elif ch == 2:
   
	print(a-b)

elif ch == 3:
  
	print(a*b)

elif ch == 4:
   
	if b == 0:
     
		print("infinity")
  
	else:
        
		print(a/b)    

elif ch == 5:
    
	print(a%b)

else:
    
	print("invalid")