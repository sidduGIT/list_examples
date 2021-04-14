mat=[[1,2,3],
     [4,5,6],
     [7,8,9]]

mat1=[[1,2,3],
     [4,5,6,10],
     [7,8,9]]

print [row[1] for row in mat]
print

print [col for row in mat for col in row]
print

print [col for row in mat for col in row if col%2]
print

print [col for row in mat1 if len(row)==3 for col in row if col%2]
print
