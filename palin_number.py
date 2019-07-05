num=int(input("Enter the number::"))
temp=num
pal=0
while num>0:
    a=num%10
    pal=pal*10+a
    num=num//10
if pal==temp:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
