import pickle
def bin2tup():
             f = open("PL.dat","wb")
             t = ('C','C++','Java','Python')
             pickle.dump(t,f)
             f.close()
             f = open("PL.dat","rb")
             d = pickle.load(f)
             print("PL1:",d[0])
             print("PL2:",d[1])
             print("PL3:",d[2])
             print("PL4:",d[3])
             f.close()
bin2tup()
