"""my_list=[]

my_list.append(5)
my_list.append(51)
my_list.append(511)
my_list.append(5111)
my_list.append(51111)

num=input("Enter a number to search in list")

if num in my_list:
    print "Number present in list"
    print my_list.index(num)
else:
    print "Number NOT present in list"

print my_list
print list(reversed(my_list))"""

alist=["ab","cd","ef","gh"]
alist.reverse()
print "New List:",alist
for i in range(len(alist)):
    print i,alist[i]
