import pickle
rec=[]
def file_create():
    f=open("student.dat","wb")
    rno = int(input("Enter Student No:"))
    sname = input("Enter Student Name:")
    address = input("Enter Address:")
    rec=[rno,sname,address]
    pickle.dump(rec,f)
def read_data():
    f = open("student.dat","rb")
    print("*"*78)
    print("Data stored in File....")
    rec=pickle.load(f)
    for i in rec:
        print(i)
file_create()
read_data()
