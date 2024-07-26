s=input("enter a string ")
l=len(s)
j=l-1
f=True
for i in range(0,l//2):
    if s[i]!=s[j]:
        f=False
        break
    j=j-1
if f==True:
    print("string is a palindrom ")
else:
    print("string is not a palindrom")
