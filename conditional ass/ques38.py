#Write a Python program to display astrological sign for given date of birth.
date=int(input("Enter the date:"))
month=input("Enter the month name:")
if month=="January":
    if date<20:
        print("Capricorn")
    else:
        print("Aquaria")
elif month=="Febraury":
    if date<19:
        print("Aquaria")
    else:
        print("Pisces")
elif month=="March":
    if date<21:
        print("Pisces")
    else:
        print("Aries")
elif month=="April":
    if date<20:
        print("Aries")
    else:
        print("Tarus")
elif month=="May":
    if date<21:
        print("Tarus")
    else:
        print("Gemini")
elif month=="June":
    if date<21:
        print("Gemini")
    else:
        print("Cancer")
elif month=="July":
    if date<23:
        print("Cancer")
    else:
        print("Leo")
elif month=="August":
    if date<23:
        print("Leo")
    else:
        print("Virgo")
elif month=="September":
    if date<26:
        print("Virgo")
    else:
        print("Libra")
elif month=="October":
    if date<23:
        print("Libra")
    else:
        print("Scorpio")
elif month=="November":
    if date<22:
        print("Scorpio")
    else:
        print("Sagittarius")
else:
    if date<22:
        print("Sagittarius")
    else:
        print("Capricorn")
