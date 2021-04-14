lst=[1,2,2,3,4,4,5,6,7,7,7,8,9]
print("original list\n",lst)
nlst=[]
duplicate=[]
for i in lst:
    if i not in nlst:
        nlst.append(i)
    else:
        duplicate.append(i)
print("non duplicate list\n",nlst)
print("duplicate list\n",duplicate)

lst=[1,2,2,3,4,4,5,6,7,7,7,8,9]
dct1={}
for i in lst:
    if i not in dct1:
        dct1[i]=1
    else:
        dct1[i]=dct1[i]+1
print(dct1)