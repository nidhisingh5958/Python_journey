r = float(input("Radius of circle:"))
print("1) 3.14")
print("2) 22/7")
v = int(input("Choose the value of pi:"))

if v == 1:
              a = 3.14*(r)**2
              print ("Area of circle:",a)
elif v == 2:
             a = 22/7*(r)**2
             print ("Area of circle:",a)
else:
             print("Invalid Input")
#alternate code
'''r=float(input("Radius of circle:"))
import math
a=math.pi*(r)**2
print ("Area of circle:",a)'''
