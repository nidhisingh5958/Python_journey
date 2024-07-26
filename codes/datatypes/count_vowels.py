s=input("enter a string ")
l=s.split()
c=0
for i in l: 
    if i[0] in "aeiou" or i[0]in"AEIOU":
        c=c+1
        print(i)
print("total words starting from vowels ",c)
