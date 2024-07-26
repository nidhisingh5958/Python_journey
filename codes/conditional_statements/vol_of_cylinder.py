r=float(input("Radius of cylinder:"))
h=float(input("Height of cylinder:"))
print("1) 3.14")
print("2) 22/7")
v = int(input("Choose the value of pi:"))

if v == 1:
              vol = 3.14*(r)**2*(h)
              print ("Area of cylinder:",vol)
elif v == 2:
             vol = 22/7*(r)**2*(h)
             print ("Volume of cylinder:",vol)
else:
             print("Invalid Input")

#Alternate Code
'''r=float(input("Radius of cylinder:"))
h=float(input("Height of cylinder:"))
import math
v=math.pi*r**2*h
print("Volume of cylinder:",v)'''
