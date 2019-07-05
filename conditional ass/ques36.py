#Write a Python program to check a triangle is equilateral, isosceles or scalene.
a=int(input("Enter the first side:"))
b=int(input("Enter the second side:"))
c=int(input("Enter the third side:"))
if a==b==c:
    print("Equilateral triangle.")
elif a==b or b==c or c==a:
    print("Triangle is an isosceles.")
else:
    print("Triangle is scalene")
