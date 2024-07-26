def countevenodd (tup):
    counteven =0
    countodd =0
    for i in tup:
        if i%2==0:
            counteven+=1
        else:
            countodd+=1
    return counteven,countodd
    
tup1=()
n=int(input("Enter the total elements in a tuple:"))
for i in range(n):
    num=int(input("Enter the number:"))
    tup1=tup1+(num,)
count_stats=countevenodd(tup1)
print("Even numbers are:",count_stats[0])
print("Odd numbers are:",count_stats[1])
