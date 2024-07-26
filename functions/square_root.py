#Python module to display sq root of a no. using math module

import math
def cal_sqrt():
             number= float(input("Enter a number:"))
             sq_rt =math.sqrt(number)
             #display the sq root
             print("The square root of",number,"is",sq_rt)
cal_sqrt()
