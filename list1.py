
a = ['spam', 'eggs', 100, 1234]
print " list a=",a

# list indices start at 0,
print 'a[0]=', a[0]
print 'a[1]=', a[1]
print 'a[2]=', a[2]
print 'a[3]=', a[3]
a.append("siddu")
print 'a[4]=', a[4]
print "\n"
print 'a[-1]=', a[-1]
print 'a[-2]=', a[-2]
print 'a[-3]=', a[-3]
print 'a[-4]=', a[-4]
print 'a[-5]=', a[-5]

a[2]=a[2]+10
print " list a=",a

a[0:2]=[10,20]
print " list a=",a

a[0:2]=["siddu","santu","surabhi","atharv"]
print " list a=",a
a[:0]=a
print " list a=",a

print "length=",len(a)

a=[1,5]
b=[2,3,4]
c=[1,b,5]
print "new list=",c
print "length of c",len(c)
print c[1]
print c[1][0]


a = [66.6, 333, 333, 1, 1234.5]

print "counts of 333=",a.count(333), "counts of 66.6=",a.count(66.6), "counts of X=",a.count('x')

a.insert(2, -1) #insert @a[2]
print a

a.append(333) #appending 333 at the end
print a

print a.index(333) #first occurance of 333 a[0] indexed

a.remove(333)  #first occurance of 333 a[0] removed
print a

a.reverse()
print a

a.sort()
print a

stack = [3, 4, 5]
stack.append(6)  #appaend will add at the end
stack.append(7)
print stack

x=stack.pop() #pop will remove at the end
print "popped ",x
print stack

x=stack.pop()
print "popped ",x
x=stack.pop()
print "popped ",x
print stack


queue = ["Eric", "John", "Michael"]
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print queue

s=queue.pop(0)
print s

s=queue.pop(0)
print s

print queue


# The del statement

a = [-1, 1, 66.6, 333, 333, 1234.5]
del a[0]
print a

del a[2:4]
print a

# filter of sequence
def f(x): return x % 2 != 0 and x % 3 != 0

res=filter(f, range(2, 25))

print res


# map of sequence

def cube(x): return x*x*x

res=map(cube, range(1, 11))

print res


# reduce(func, sequence)" returns a single value constructed by
# calling the binary function func on the first two items of the sequence,
# then on the result and the next item, and so on

def add(x,y): return x+y

r=reduce(add, range(1, 11))
print r # 55

