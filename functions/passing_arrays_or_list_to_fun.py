#Arrays (list) passing to a function that calculates
#the arithmetic mean of list elements

def list_avg(st):
             l=len(st)
             sum=0
             for i in st:
                          sum+=i
             return sum/1
print("Input Integers:")
a=input()
a=a.split()
for i in range(len(a)):
             a[i]=int(a[i])

avrg=list_avg(a)

print("Average is:")
print(round(avrg,2))
