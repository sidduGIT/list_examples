str1='"Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at ' \
     'their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at ' \
     'runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings ' \
     'are interned by the interpreter) and make startup time faster."'
words=str1.split()
dict1={}
for word in words:
    if word not in dict1:
        dict1[word]=1
    else:
        dict1[word]+=1
print(dict1)
print(sorted(dict1.items(),key=lambda x:x[1]))
print(sorted(dict1.items(),key=lambda x:x[1])[-1])
print(sorted(dict1.items(),key=lambda x:x[1])[-2])
print(sorted(dict1.items(),key=lambda x:x[1])[-3])