aList = [21,8,15,27,2,80,1]
print("Original list is",aList)
n = len(aList)
for i in range(1,n):
             key = aList[i]
             i = i-1
             while i>=0 and aList[i]>key:
                          aList[i+1] = aList[i]
                          i=i-1
             aList[i+1]=key
             print("After pass",i,":",aList)
print("Sorted List is",aList)
