lst=[1,2,3,40,5,6,7]
lrg=0
sml=100
for i in lst:
    if(i>lrg):
        lrg=i
print("large number in a list=",lrg)

lst=[1,2,3,40,5,6,7]
sml=100
for i in lst:
    if(i<sml):
        sml=i
print("small number in a list=",sml)