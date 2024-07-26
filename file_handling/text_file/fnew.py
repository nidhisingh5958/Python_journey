# to perform addition of two numbers using file
f=open('new.txt','w')
num1=int(input('enter the first no.:'))
num2=int(input('enter the second no.:'))
sum1=num1+num2
f.write('\n the first no. is: '+str(num1))
f.write('\n the second no. is: '+str(num2))
f.write('\n the sum of the nos. is: '+str(sum1))
f.close
