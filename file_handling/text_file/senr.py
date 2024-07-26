t=open("new.txt","r")
line=" "
while line:
             line=t.readline()
             if line:
                          if line[0].isupper():
                                       print(line)
t.close()
