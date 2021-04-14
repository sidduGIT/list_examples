A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,3],[4,5,6],[7,8,9]]
C=[[0,0,0,],[0,0,0,],[0,0,0,]]
for row in range(len(A)):
    for col in range(len(B)):
        C[row][col]=A[row][col]+B[row][col]

print(C)
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,3],[4,5,6],[7,8,9]]
C=[[0,0,0,],[0,0,0,],[0,0,0,]]
for row in range(len(A)):
    for col in range(len(B)):
        C[row][col]=A[row][col]-B[row][col]

print(C)
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,3],[4,5,6],[7,8,9]]
C=[[0,0,0,],[0,0,0,],[0,0,0,]]
for row in range(len(A)):
    for col in range(len(B)):
        C[row][col]=A[row][col]*B[row][col]

print(C)
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,3],[4,5,6],[7,8,9]]
C=[[0,0,0,],[0,0,0,],[0,0,0,]]
for row in range(len(A)):
    for col in range(len(B)):
        C[row][col]=A[row][col]//B[row][col]

print(C)

str1 = "Python"
#str2 = "Python"
str2='Siddu'
str3='Siddu'
print("\nMemory location of str1 =", hex(id(str3)))
print("Memory location of str2 =", hex(id(str2)))
print()
