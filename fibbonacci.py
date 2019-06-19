num=int(input("Enter the range till you have tp print the fibbonacci series:"))
a=0
b=1
print(a,b , end=" ")
c=0
for r in range(2,num):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

