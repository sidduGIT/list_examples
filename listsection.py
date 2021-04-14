x=[1,2,3,4]
y=[10,2,4,12,15]
z=[]
for i in y:
    if i not in x:
        z.append(i)

print(z)

