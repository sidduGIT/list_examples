n=int(input("enter hom many items"))
counter=0
lst=[]
while n!=counter:
    i=int(input("enter a list item"))
    lst.append(i)
    counter=counter+1
print("original list",lst)
print("reversed list",lst[::-1])