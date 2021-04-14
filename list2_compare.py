lst1=[2,1,5,7,8,9]
lst2=[1,5,4,7,8,6]
sum1=lst1[0]+lst1[-1]
sum2=lst2[0]+lst2[-1]
if sum1==sum2:
    print(True)
else:
    print(False)

lst1=[2,1,5,7,8,9]
sum=0
for i in lst1:
    sum=sum+i
    avg=float(sum/len(lst1))
print("sum of all elements",sum)
print("sum of all elements",avg)

lst1=[2,1,5,7,8,9]
#lst1.sort()
sorted_list=sorted(lst1)
print(sorted_list)
lst1.sort(reverse=True)
print(lst1)

def bubble_sort(lst):
    for item_num in range(len(lst)-1,0,-1):
        for idx in range(item_num):
            if(lst[idx]>lst[idx+1]):
                temp=lst[idx]
                lst[idx]=lst[idx+1]
                lst[idx+1]=temp
lst1=[2,1,5,7,8,9]
bubble_sort(lst1)
print(lst1)
