str="siddu bagewadi"
str1=[i for i in str if i not in 'aeiou']
print(str1)

my_string = "hello world"
k = [(i.upper(), len(i)) for i in my_string]
print(k)

x = [i**+1 for i in range(3)]; print(x);

print([i+j for i in "abc" for j in "def"])

l=[3,-9,5,-4,7,-1,4,-2]
print([x for x in l if x<0])

s=["pune", "mumbai", "delhi"]
print([(w.upper(), len(w)) for w in s])

l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print([i**3 for i in l])

l=[[1 ,2, 3], [4, 5, 6], [7, 8, 9]]
print([[row[i] for row in l] for i in range(3)])

w="hello"
v=('a', 'e', 'i', 'o', 'u')

print([x for x in w if x in v])

l=["good!", "oh", "excellent!", "450"]
print([n for n in l if n.isalpha() or n.isdigit()])

d ={'john':40, 'peter':45}
try:
    print(d['siddu'])
except:KeyError

a={1:"A",2:"B",3:"C"}
b=a.copy()
b[2]="D"
print(a)
print(b)

a={1:"A",2:"B",3:"C"}
print(a.items())

a={1:"A",2:"B",3:"C"}
a.items()

a = {}
a[1] = 1
a['1'] = 2
a[1]=a[1]+1
print(a)
count = 0
for i in a:
    print(a[i])
    count += a[i]
print(count)

