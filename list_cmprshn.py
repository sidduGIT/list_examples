list1=[2,3,4]
list2=[]
for i in list1:
    list2.append(i*4)
print(list2)

list2=[i*4 for i in list1]
print(list2)

str="hai atharv super boy"
list1=str.split()
list2=[i.upper() for i in list1]
print(list2)

str="hai atharv 12345 super boy"
#list1=str.split()
list2=[i for i in str if(i.isdigit())]
print(list2)

str="hai atharv 12345 super boy"
list1=str.split()
list2=[i.upper() for i in list1]
print(list2)