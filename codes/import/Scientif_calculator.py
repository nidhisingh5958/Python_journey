import math 
print(""" 
select -  
1 - Addition(x, y) 
2 - subtraction(x,y) 
3-multiplication(x,y) 
4 - division(x, y) 
5- exponent(x, y) 
6 - tan(x) 
7 - sin(x) 
8 - cos(x) 
9 - factorial(x) 
10 - log(x) 
11 - sqrt(x)
""") 

def val():
    x = int(input("Enter the number:"))
    return(x)
def value():
    y = int(input("2nd number -")) 
    return(y)

o = input("") 
if o == "1": 
    print(val()+value()) 
elif o == "2": 
    print(val()-value()) 
elif o == "3": 
    print(val()*value()) 
elif o == "4": 
    print(val()/value()) 
elif o == "5": 
    print(val()**value()) 
elif o == "6": 
    print(math.tan(val()))
elif o == "7": 
    print(math.sin(val()))
elif o == "8": 
    print(math.cos(val())) 
elif o == "9": 
    print(math.factorial(val())) 
elif o == "10": 
    print(math.log(val()))
elif o == "11":
    print(math.sqrt(val()))
