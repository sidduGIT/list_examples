arr=[[1,2,3],[4,5,6],[7,8,9]]
#arr=[[1,1,1],[1,1,1],[1,1,1]]
sum1=sum2=0
for i in range(3):
    for j in range(3):
        if (i+j)==2:
            sum2 += arr[i][j]
        if i==j:
            sum1+=arr[i][j]

print(arr)
print(sum1)
print(sum2)
print(abs(sum1-sum2))

arr=[[1,2],[3,4]]
narr=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        narr[i][j]=5*arr[i][j]
print(narr)


