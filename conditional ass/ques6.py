#Write a Python program to count the number of even and odd numbers from a series of numbers.
a=int(input("Enter the number of elements in the list"))
print("Enter the list")
l=[]
countev=0
countodd=0
for i in range(a):
    b=int(input())
    l.append(b)
for i in range(a):
    if l[i]%2==0:
        countev+=1
    else:
        countodd+=1
print("No. of even elements:",countev)
print("No. of odd elements:",countodd)
