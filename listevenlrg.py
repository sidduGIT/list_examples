lst=[3,7,1,8,9,20,12,18,40,34]
elst=[]
olst=[]
for i in lst:
    if(i%2==0):
        elst.append(i)
    else:
        olst.append(i)
print("even list is",elst)
print("odd list is",olst)
elst.sort()
olst.sort()
print("even list after sorting is",elst)
print("odd list after sorting is",olst)
print("largest of elst",elst[-1])
print("largest of olst",olst[-1])
print("second largest of elst",elst[-2])
print("second largest of olst",olst[-2])
print("smallest of elst",elst[0])
print("smallest of olst",olst[0])
print("merge of both list",elst+olst)
mlst=elst+olst
mlst.sort()
print("sorted after merging",mlst)