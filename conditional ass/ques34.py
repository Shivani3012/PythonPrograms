#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
def sum(a,b):
    sum=a+b
    if sum>=15 and sum<=20:
        return 20
    else:
        return sum
a=int(input("Enter the first number:"))
b=int(input("Enter theb second number:"))
sum1=sum(a,b)
print(sum1)
