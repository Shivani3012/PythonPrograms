p=input("Enter the  string::")
a=len(p)
s=""
for i in range(a-1,-1,-1):
    s=s+p[i]
if s==p:
    print("The string is palindrome")
else:
    print("The string is not palindrome.")

    
