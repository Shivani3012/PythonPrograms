#Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be
#printed in a comma-separated sequence.
for i in range(100,401):
    b=str(i)
    if (int(b[0])%2==0 and int(b[1])%2==0 and int(b[2])%2==0):
        print (b , end=",")
    



