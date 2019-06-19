print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")
print("5) Power")
ch=int(input("Enter the operation you want to perform"))
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if ch==1:
    c=a+b
    print("Addition of two numbers is",c)
elif ch==2:
    if a>b:
        c=a-b
        print("Difference between %s and %s is %s",(a,b,c))
    else:
        c=b-a
        print("Difference between %s and %s is %s",(b,a,c))
elif ch==3:
    c=a*b
    print("Product of two numbers is ",c)
elif ch==4:
    c=a//b
    print("Value after dividing of two values",c)
else:
    c=a**b
    print("Power of %s is",(a,c))
