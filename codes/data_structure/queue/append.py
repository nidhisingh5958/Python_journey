Student=[]
def QueueUp(Student):
              name = input('Enter Name')
              Student.append(name)
def QueueDisp(Student):
              if len(Student)==0:
                           print('Underflow')
              else:
                           print('Queue Items Front-to-Rear')
                           for i in range(len(Student)):
                                        print(Student[i])
