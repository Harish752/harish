n=input()
i=len(n)
s=0
for x in n:
  s=s+int(x)**i
if str(s)==str(n):
  print("yes")
else:
  print("no")