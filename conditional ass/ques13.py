#Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a
#comma separated sequence.
print("Enter the 4 digits binary numbers:")
l=[]
l1=[]
for i in range(0,4):
    b=int(input())
    l.append(b)
print(l)
for i in range(0,4):
    if l[i]%5==0:
        print(l[i])
    else:
        l1.append(l[i])

        
        
