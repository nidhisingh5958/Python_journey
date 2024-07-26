from time import gmtime, strftime
n=strftime("%a, %d %b %Y", gmtime())
n=str(n)
today=n[5:]
print(n)
