n=int(input("enter a num"))
l=[]
while(n>0):
    dig=n%10
    l.append(dig)
    n=n//10
#l.reverse()
reversed(l)
print ("list",l)
l=[str(i) for i in l]
print(''.join(l))