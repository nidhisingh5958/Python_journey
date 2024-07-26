N=input("Enter a string")
l=len(N)
r=""
print("Orignal : ",N)
for x in range(l):
    if N[x].islower():
        r+=N[x].upper()
    else:
        if N[x].isupper():
            if x%2==0:
                r+=N[x].lower()
            else:
                r+=N[x-1]
print("Final : ",r)
