a=int(input("Enter the number of elements in the list"))
print("Enter the list")
l=[]
for i in range(a):
    b=int(input())
    l.append(b)
print(l)
l.sort()
print(l)
las=a-1
seclar=las-1
sesma=1
print("Second smallest number in the list is",l[sesma])
print("Second largest number in the list is",l[seclar])

