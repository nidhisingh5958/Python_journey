noNames={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
num=input("Enter any number:")
result=' '
for ch in num:
             key= int(ch)
             value= noNames[key]
             result= result + ' ' + value
print("The number is:",num)
print("The numberName is:",result)
             
             
