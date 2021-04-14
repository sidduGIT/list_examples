lst=[10,20,30,40,50,60]
print("list before swapping first and last",lst)
'''temp=lst[0]
lst[0]=lst[-1]
lst[-1]=temp
print("list after swapping first and last",lst)

temp=lst[1]
lst[1]=lst[-2]
lst[-2]=temp
print("list after swapping first and last",lst)'''

lst[0],lst[-1]=lst[-1],lst[0]
print("list after swapping first and last",lst)