#Write a Python program to check a string represent an integer or not.
s=input("Enter the string")
a=s.isdigit()
#print(a)
if a==True:
    print("This is  an integer.")
else:
    print("This is not an integer.")
