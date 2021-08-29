n= int(input("enter the number of rows:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end="")
    print()
print("")
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end="")
    print()
    
print("")
for i in range(n):
    print(" "*i+"*"*(n-i))

print("")

for i in range(n):
    print((n-i)*" "+i*"*")
