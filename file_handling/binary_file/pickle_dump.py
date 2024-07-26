def bin_create():
             import pickle
             list1=[40.50,67,39,42,95,897,674,125]
             f=open("list.daf",'wb')
             pickle.dump(list1,f)
             print("Information added to Binary File")
             f.close()
bin_create()
