#Write a Python program to get the Fibonacci series between 0 to 50.
a=0
b=1
print(a,b , end=" ")
c=0
for r in range(2,10):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

