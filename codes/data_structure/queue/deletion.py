Student=[]
def QueueUp(Student):
             name = input('Enter any name')
             Student.append(name)
def QueueDel(Student):
              if len(Student)==0:
                           print('Underflow')
              else:
                           name = Student.pop(0)
                           print('Deleted Name was ',name)
