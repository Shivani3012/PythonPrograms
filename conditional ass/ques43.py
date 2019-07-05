#. Write a Python program to create the multiplication table (from 1 to 10) of a number.
n=int(input("Enter the number between 1 to 10 to print the table:"))
for i in range(1,11):
    print("%s X %s = %s" %(n,i,n*i))
