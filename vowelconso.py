ch = input("Enter a character: ")

if(ch=='a' or ch =='e' or ch=='i' or ch=='o'  or ch=='u'):
    print(ch, "Vowel")
elif ch.isalpha():
    print(ch, "Consonant")
else:
    print(ch,"invalid")