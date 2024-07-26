val = [10,20,30,40,1,2,3,100,200,10,20,30,11,12,15,17,19,90,77,35]
slice1 = val[5:15:2]
slice2 = val[::4]
sum = 0
for x in slice1 :
             print(x,"==",end=' ')
             sum+=x
print("Sum of slice1 elements are",sum)

sum=0
for x in slice2:
             print(x,"==",end=' ')
             sum+=x
avg = sum / len(slice2)
print("Average of slice2=",avg)
