x=[1,2,3,4]
y=[10,11,12]
lst=[]
for i in x:
    for j in y:
      lst.append(i+j)

print(lst)

lst=[i+j for i in x for j in y]
print(lst)

lst=[i*j for i in x for j in y]
print(lst)


