#Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
month=input("Enter the month name::")
day=int(input("Enter the day:"))
if month in ("December","January","Febraury"):
    print("Season is Winter.")
elif month in ("March","April","May"):
    print("Season is Spring.")
elif month in ("June","July","August"):
    print("Season is Summer.")
else:
    print("Season is Autumn.")
