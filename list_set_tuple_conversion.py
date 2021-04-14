mylist=[1,2,3,4,5,6,7,8,8,4,3,2]
print("original list\n",mylist)

set1=set(mylist)
print("after convertng list to set\n",set1)

tup1=tuple(mylist)
print("after convertng list to tuple\n",tup1)

set1={1,2,3,4,5,6}
print("original set\n",set1)

set_2_list=list(set1)
print("after convertng set to list\n",set_2_list)

set_2_tuple=tuple(set1)
print("after convertng set to tuple\n",set_2_tuple)

tup1=(1,2,3,4,5,6)
print("original tuple\n",tup1)

tuple_2_list=list(tup1)
print("after convertng tuple to list\n",set_2_list)

tuple_2_set=set(tup1)
print("after convertng tuple to set\n",set_2_tuple)



