list_rivers=["Ganges", "Godavari", "Brahmaputra", "Narmada", "Yamuna", "Mahanadi", "Kaveri", "Tapti"]
nlist=[]
dict1={}
for i in list_rivers:
    nlist.append(len(i))
print("new list containing number of chars in a list_rivers\n",nlist)
dict1=dict(zip(list_rivers,nlist))
print("creation of dictionery from chars and its numbers in list_rivers\n",dict1)

rivers_list=[]
char_nums=[]
for rivers,char_num in dict1.items():
    rivers_list.append(rivers)
    char_nums.append(char_num)
print("converting back to list of rivers",rivers_list)
print("converting back to its chars numbers",char_nums)
