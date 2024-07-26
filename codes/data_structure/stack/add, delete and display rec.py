#Program to add, delete and display the records of an Employee using list implementation through Stack
Emplyee=[]
c="y"
while (c=="y"):
             print ("1.PUSH")
             print ("2.POP")
             print("3.DISPLAY")
             choice=int(input("Enter your choice:"))
             if (choice==1):
                          e_id=input("Enter your choice:")
                          ename=input("Enter the employee name:")
                          emp= (e_id,ename)
                          Employee.append(emp)
             elif (choice==2):
                          if (Employee==[]):
                                       print ("Stack Empty")
                          else:
                                   e_id,ename=Employee.pop()
                                   print("Deleted element is:",e_id,ename)
             elif (choice==3):
                          i=len(Employee)
                          while i>0:
                                       print (Employee[i-1])
                                       i=i-1
             else:
                          print("Wrong Input")
             c=input("Do you want to continue or not?")
 
