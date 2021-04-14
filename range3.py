l=[]
for i in range(200,400):
    if(i%7==0) & (i%5!=0):
        l.append(str(i))
print (",".join(l))