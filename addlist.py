lst=[1,2,3,-4,5,-6,0,-7,8,0,9,11]
ecnt=0
ocnt=0
ncnt=0
zcnt=0
zeros=0
for i in lst:
    if(i<0):
        ncnt += 1
    elif(i%2==0):
        ecnt+=1
    elif(i==0):
        zcnt+=1
    else:
        ocnt+=1
    #print(i)

print("ecnt=",ecnt,"ocnt=",ocnt,"ncnt=",ncnt,"zcnt=",zcnt)
