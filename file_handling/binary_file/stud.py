import pickle
def search_95plus():
    f = open("marks.dat","ab")
    while True:
        rn=int(input("Enter the rollno:"))
        sname=input("Enter the name:")
        marks=int(input("Enter the marks:"))
        rec=[]
        data=[rn,sname,marks]
        rec.append(data)
        pickle.dump(rec,f)
        ch=input("Want more records?Yes:")
        if ch.lower() not in 'yes':
           break
    f.close()
    f = open("marks.dat","rb")
    cnt=0
    try:
        while True:
            data = pickle.load(f)
            for s in data:
               if s[2]>95:
                   cnt+=1
                   print("Record:",cnt)
                   print("RollNO:",s[0])
                   print("Name:",s[1])
                   print("Marks:",s[2])
    except Exception:
        f.close()
search_95plus()  
