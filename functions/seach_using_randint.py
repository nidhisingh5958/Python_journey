#Binary Search using randint
from random import randint
def bin_search(st,item):
             mid= len(st)//2
             low=0
             high=len(st)-1
             while st[mid]!= item and low<=high:
                          if item>st[mid]:
                                       low=mid+1
                          else:
                                       high=mid-1
                          mid=(low+high)//2
             if low>high:
                          return None
             else:
                          return mid
a=[]
for i in range(10):
             a.append(randint(1,20)) #list elements within the range gets automatically generated
a.sort()           #sort() used to arrange the list elements is ascending order
print(a)

value= int(input('Enter the number to be searched:'))
#index= bin_search(a,value)
print("Element found at the index:",bin_search(a,value))
