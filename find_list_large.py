mylist=[5,1,7,10,8,50]
large=1
for i in mylist:
    if(i>large):
        large=i
print("largest number in list",large)
#print(mylist)

mylist=[5,1,7,10,8,50]
small=7
for i in mylist:
    if(i<small):
        small=i
print("smallest number in list",small)

mylist=[5,1,7,10,8,50]
find=2
for i in mylist:
    if(i==find):
        print(find,"number found")
        break
else:
    print(find,"number not found")

mylist=[5,1,7,10,8,50]
print(sorted(mylist))
leng=len(mylist)
print(leng)
print("first largeet", mylist[leng-1])
print("second largeet", mylist[leng-2])
print("second largeet", mylist[-2])

a=[]
n=int(input("enter how many elements in list"))
for i in range(1,n+1):
    ele=int(input("enter a element"))
    a.append(ele)
print("list",a)
a.sort()
print("list",a)
print("second largest",a[n-2])
