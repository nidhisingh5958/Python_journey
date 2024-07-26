a=input("Your name:")
print("Marks out of:")
outof =int(input())

print("Enter Marks Obtained in 5 Subjects: ")
mOne = int(input())
mTwo = int(input())
mThree = int(input())
mFour = int(input())
mFive = int(input())

sum = mOne+mTwo+mThree+mFour+mFive
perc = (sum/(5*outof))*100

print("Percentage:",perc)

if perc>=95:
             print("O")
elif perc>=90 and perc<95:
             print("A+")
elif perc>=85 and perc<90:
             print("A")
elif perc>=80 and perc<85:
             print("B+")
elif perc>=75 and perc<80:
             print("B")
elif perc>=60 and perc<75 :
             print("Average Score")
else:
             print("Needs improvement")
