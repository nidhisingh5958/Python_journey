numbers= tuple()
n=int(input("How many numbers you want to enter? :"))
for i in range(0,n):
             num=int(input())
             numbers= numbers + (num,)
print('\nThe numbers in the tuple are:')
print(numbers)
print("\nThe maximum number is:")
print(max(numbers))
print("The minimum number is:")
print(min(numbers))
print("The sum of the tuple elements:")
print(sum(numbers))
mean=sum(numbers)/len(numbers)
print("The mean of values in the tuple is:")
print(mean)

