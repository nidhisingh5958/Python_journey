#Function for calculating factorial of a number using return
def calc(a,b):
             add = a+b
             sub = a-b
             mul = a*b
             div = a/b
             return add,sub,mul,div       #returning multiple values return statement
result = calc(500,40)
print(result)
print("The result can be displayed as:")
for i in result:                 #displaying multiple values returned as the output
             print(i)
