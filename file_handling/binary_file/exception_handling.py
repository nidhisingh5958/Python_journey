try:
             f=open("gnew.txt",'r')
             print(f.read())
             f.close()
except FileNotFoundError:
             print("No such file exists")
