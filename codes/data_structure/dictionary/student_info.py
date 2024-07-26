sd=dict()
i=1
f=0
n=int(input("Enter number of entries:"))
while i<=n:
             adm=input("\nEnter admission no of the student:")
             nm=input("Enter name of the student:")
             sec=input("Enter class and section:")
             per=float(input("Enter percentage of a student:"))
             b=(nm,sec,per)
             sd[adm]=b
             i=i+1
l=sd.keys()
for i in l:
             print("\nAdm no- ",i,":")
             z=sd[i]
             print("Name\t","class\t","per\t")
             for j in z:
                          print(j, end="\t")
                      
             
                          
