from csv import reader
def pro2():
             with open("emp.csv","r") as f:
                          d = reader(f)
                          data=list(d)
                          for i in data:
                                       print(', '.join(i))
pro2()
