pal=input("Enterthe number or string")
flag=0
a=len(pal)
beg=0
back=a-1
while beg<=back:
    if pal[beg]!=pal[back]:
        flag=0
    else:
        flag=1
    beg=beg+1
    back=back-1
if flag==1:
    print("palindrome")
else:
    print("Not palindrome")
    
