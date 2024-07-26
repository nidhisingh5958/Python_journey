# program to pass a dictionary to a function eith list of elements as keys
#and frequency of its occurance as value and return as a dictionary

def frequencyCount(list1,dict):
             for i in list1:
                          if i not in dict:
                                       dict[i]=1
                          else:
                                       dict[i]+=1
             return dict

list1=[4,5,6,510,6,5,5,40,30,2,4]
d={}
frequencyCount(list1,d)
print(d)
