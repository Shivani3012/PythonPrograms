# Write a Python program that accepts a string and calculate the number of digits and letters.
w=input("Enter the string:")
l=len(w)
w.split(" ")
dc=0
lc=0
for i in range(l):
    if w[i].isalpha()==True:
        lc+=1
    else:
        dc+=1
print("Number of letters is",lc)
print("Number of digits is",dc)
