num=int(input("Enter the number"))
s=0
temp=num
while num>0:
    n=num%10
    s+=n**3
    num=num//10
if temp==s:
    print("The number is armstrong.")
else:
    print("The number is not armstrong.")
    
