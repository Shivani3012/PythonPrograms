#Write a Python program to convert month name to a number of days.
print("Enter the list of the month names:")
lname=[]
for i in range(0,12):
    b=input()
    lname.append(b)
#print(lname)
m=input("Enter the month name:")
ind=lname.index(m)
#print(ind)
if ind==0 or ind==2 or ind==4 or ind==6 or ind==7 or ind==9 or ind==11:
    print("number of days in "+ m +" is 31")
elif ind==1:
    print("number of days in febraury is 28/29")
else:
    print("number of days "+m+" is 30")
    
