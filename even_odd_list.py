mylist=[3,1,2,6,7,24,25,34,67,80,100,103]
elist=[]
olist=[]
for i in mylist:
    if(i%2==0):
        elist.append(i)
    else:
        olist.append(i)
elist.sort()
olist.sort()
print(elist)
print(olist)

list1=[4,3,7,12,6]
list2=[7,23,45,56,67]
mlist=list1+list2
print(mlist)
mlist.sort()
print(mlist)
