def percentage_calc(mOne,mTwo,mThree,mFour,mFive):
    sum = mOne+mTwo+mThree+mFour+mFive
    perc = (sum/500)*100

a=input("Your name:")
print("Enter Marks Obtained in 5 Subjects: ")
mOne = int(input())
mTwo = int(input())
mThree = int(input())
mFour = int(input())
mFive = int(input())

percentage_calc(mOne,mTwo,mThree,mFour,mFive)

print(end="Total = ")
print(sum)
print(end="Percentage Mark = ")
print(perc)

