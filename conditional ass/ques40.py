#Write a Python program to find the median of three values.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
l=[a,b,c]
l.sort()
print("The median value is ",l[1])
