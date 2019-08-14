try:
	o=int(input())
	if(o%2==0):
		print(o//2)
	else:
		print(o)
except ValueError:
	print("invalid")
