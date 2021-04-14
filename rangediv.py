low=int(input("enter lower num"))
upp=int(input("enter upper num"))
n=int(input("enter number to be devisive"))
for i in range(low,upp+1):
    if(i%n==0):
        print(i)
