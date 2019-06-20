s=input()
i=0
for a in range (len(s)):
 if(s[a].isdigit() or s[a].isalpha() or s[a]==' '):
  continue
 else:
  i+=1
print(i) 