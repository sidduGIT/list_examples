def lst2(lst1,lst2):
    result=False
    for i in lst1:
        for j in lst2:
            if i==j:
                result=True
    return result
print(lst2([1,2,3,7],[8,4,6,11,13]))