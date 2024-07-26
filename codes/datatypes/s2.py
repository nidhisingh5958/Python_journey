s=input("enter a string")
l=s.split()
mx=0
k=0
mxword=""
for i in l:
             k=len(i)
             if k>mx and i.isalpha()==True:
                          mxword=i
                          mx=k
print()
print("substring with maximum length is:",mxword)
print("and its length is",k)
