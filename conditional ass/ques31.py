#Write a Python program to calculate a dog's age in dog's years.
n=int(input("Enter the dog's age in human's years:"))
if n<=2:
    age=n*10.5
    print("The age of the dog in dog's years is:",age)
else:
    age=(2*10.5)+((n-2)*4)
    print("The age of the dog in dog's years is:",age)
