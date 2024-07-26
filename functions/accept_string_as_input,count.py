#accept, count the no. of times a character is present inside it
def countchar(str,ch):
             count=0
             for i in str:
                          if i==ch:
                                       count+=1
             return count
#function call
str_input= input("Enter any string:")
ch1=input("Enter the character to count:")
result=countchar(str_input,ch1)
if result==0:
             print(ch1,"does not exist in the string")
else:
             print(ch1,"exist",result,"times in the string")
