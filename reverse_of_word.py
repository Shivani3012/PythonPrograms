# Write a Python program that accepts a word from the user and reverse it.
s=input("Enter the word:")
a=len(s)
s1=""
for i in range(a-1,-1,-1):
    s1=s1+s[i]
print("Word in reverse order is",s1)

