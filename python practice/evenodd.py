a=int(input("Enter the number:"))
if a%2==0:
    print("The number is even.")
else:
    if a>1:
        for i in range(2,a):
            if a%i==0:
                print("The number is not a program.")
            else:
                print("The number is a prime number.")
                break
    else:
        print("The number is prime number.")
