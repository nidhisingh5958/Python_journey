# fibonacci series
i = int(input("How many terms? "))
b, c = 0, 1
nterms = 0
while nterms <= i:
             print(b)
             a = b + c
             b = c
             c = a
             nterms+=1
       
