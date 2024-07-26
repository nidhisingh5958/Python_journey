rc=open("new.txt","w")
line=" "
while line !="END":
             line=input("Enter a sentence or type END to end:")
             rc.write(line+"\n")
rc.close()
             
