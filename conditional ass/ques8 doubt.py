#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
n=0
while n<=6:
    print(n)
    n+=1
    if n==3 and n==6:
        continue
