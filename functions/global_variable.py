def fun(x,y):
    global a
    a=10
    print(id(a))
    x,y=y,x
    b=20
    b=30
    c=30
    print(a,b,x,y)
a,b,x,y=1,2,3,4
t=(id(a))
fun(50,100)
print(a,b,x,y)
print(id(a))
