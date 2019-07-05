#Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
n=int(input("Enter the number of integers you have to find sum and average:"))
print("Enter the numbers:")
s=0
c=0
for i in range(n):
    b=int(input())
    if b==0:
        break
    s=s+b
    c+=1
a=s//c
print(s)
print(a)
