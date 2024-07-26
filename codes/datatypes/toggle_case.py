s=("COMputEr")
l=len(s)
c=0
r=" "
for i in range(l):
             if s[i].isupper():
                          r=r+s[i].lower()
             elif s[i].islower():
                          r=r+s[i].upper()
             else:
                          r=r+[i]
print("new string",r)
