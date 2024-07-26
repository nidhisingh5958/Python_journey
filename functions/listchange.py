def listchange(arr,n):
             l=len(arr)
             for a in range(l):
                          if (arr[a]%2==0):
                                       arr[a]=10
                          else:
                                       arr[a]=arr[a]*5
a=[10,20,23,45]
listchange(a,4)
print(a)
