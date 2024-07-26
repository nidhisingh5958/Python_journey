#Program to add, delete and disploy the records of an Employee using list
Employee=[]
c='y'
while (c=='y'):
             print("1. Push")
             print("2. Pop")
             print("3. Display")
             choice=int( input("Enter your choice:"))
             if (choice==1):
                          e_id=input("Enter Employee no:")
                          ename=input("Enter Employee name:")
                          emp= (e_id,ename)
                          Employee.append(emp)
             elif(choice==2):
                          if (Employee==[]):
                                       print("Stack Empty")
                          else:
                                       e_id,ename=Employee.pop()
                                       print("Deleted element is:",e_id,ename)
             elif (choice==3):
                          l=len(Employee)
                          while l > 0:  # To print elements from last to first
                                       print(Employee[l-1])
                                       l=l-1
             else:
                          print("Wrong Input")
             c=input("Do you want to continue or not?")
