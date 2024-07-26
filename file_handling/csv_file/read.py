from csv import reader
def pro1():
             with open('top5.csv','r') as f:
                          d = reader(f)
                          data=list(d)
                          for i in data:
                                       print(i)
pro1()
