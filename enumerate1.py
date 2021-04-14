# Python program to illustrate 
# enumerate function 
l1 = ["eat", "sleep", "repeat"]
print(list(enumerate(l1)))

# changing start index to 2 from 0 
print(list(enumerate(l1, 2)))

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
ncolor=[]
for i,x in enumerate(color):
    print (i,x)
    #print(x)
    if i not in (0,4,5):
        ncolor.append(x)
print(ncolor)