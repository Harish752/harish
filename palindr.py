def checkPalindrome(str) : 
      
    n = len(str) 
      
    # Counting number of  
    # characters that  
    # should be changed. 
    count = 0
    for i in range(0, int(n / 2)) : 
        if (str[i] != str[n - i - 1]) : 
            count = count + 1
      
    # If count of changes  
    # is less than 
    # or equal to 1 
    if(count <= 1) : 
        return True
    else : 
        return False
  
# Driver Code 
str = str(input())
if (checkPalindrome(str)) : 
    print ("Yes") 
else : 
    print ("No") 
