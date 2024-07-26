#To calculate power of a number using recursion
def power(x,n):
             if n==0:
                          return 1
             else:
                          return x*power(x,n-1)
a=2
print(power(a,4))
