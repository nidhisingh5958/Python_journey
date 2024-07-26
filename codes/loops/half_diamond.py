n = 5
for a1 in range (0,n):
    for a2 in range (a1):
        print("*", end="")
    print()
for a1 in range (n,0,-1):
    for a2 in range (a1):
        print("*", end="")
    print()
