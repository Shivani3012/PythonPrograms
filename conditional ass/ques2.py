# Write a Python program to convert temperatures to and from celsius, fahrenheit.
print("1. Conversion of temperature from celsius to fahrenheit.")
print("2. Conversion of temperature from fahrenheit to celsius.")
ch=int(input("Enter the choice:"))
if ch==1:
    c=int(input("Enter the temperature in celsius:"))
    f=(c*9/5)+32
    print("Temperature in fahrenheit is ",f)
else:
    f=int(input("Enter the temperature in fahrenheit:"))
    c=((f-32)*5)/9
    print("Temperature in celsius:",c)
