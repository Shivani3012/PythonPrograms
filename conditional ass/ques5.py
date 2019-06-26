#Write a Python program that accepts a word from the user and reverse it.
word=input("Enter the word:")
a=len(word)
s=""
for i in range(a-1,-1,-1):
    s=s+word[i]
print("Word in the reverse order is ",s)
