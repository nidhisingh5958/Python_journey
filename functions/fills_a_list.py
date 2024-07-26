#a function that fills a list with numbers

from random import randint
def fill_list(st,limit_num,low,high):
             for i in range(limit_num):
                          st.append(randint(low,high))
minimum = int(input("Min:"))
maximum = int(input("Max:"))
n=int(input("Numbers limit:"))
a=[]       #an empty list
fill_list(a,n,minimum,maximum)
print(a)    #prints the newly created list
