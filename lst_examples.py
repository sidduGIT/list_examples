# #Write a Python program to sum all the items in a list.
# #
# # lst=[1,2,3,4,5,6,7,8,9]
# # print(sum(lst))
# # sum1=0
# # for i in lst:
# #     sum1+=i
# # print(sum1)
# #
# # print(sum([i for i in lst if i%2==0]))
# # print(sum([i for i in lst if i%2!=0]))
#
# # Write a Python program to multiplies all the items in a list.
# # lst=[1,2,3,4,5,6,7,8,9]
# # prod=1
# # for i in lst:
# #     prod*=i
# # print(prod)
# # prod=1
# # for i in range(1,100):
# #     prod*=i
# # print(prod)
#
# #Write a Python program to get the largest number from a list
# # lst=[2,56,89,234,68,456,98,75,678]
# # max1=lst[0]
# # for i in lst:
# #     if i>max1:
# #         max1=i
# # print(max1)
# # print(max(lst))
# #
# # min1=1000
# # for i in lst:
# #     if i<min1:
# #         min1=i
# # print(min1)
# # print(min(lst))
#
# #Write a Python program to count the number of strings where the string length is 2 or
# # more and the first and last character are same from a given list of strings.
#
# # str1='''Write a Python program to count the number of strings where the string length is 2 or
# # more and the first and last character are same from a given list of strings'''
# # words=str1.split()
# # print(([i for i in words if len(i)>4]))
# # print(len([i for i in words if len(i)>4]))
# #
# # print(([i for i in words if len(i)<4]))
# # print(len([i for i in words if len(i)>4]))
# #
# # print(([i for i in words if len(i)>2 and i[0]==i[-1]]))
# # print(len([i for i in words if len(i)>4and i[0]==i[-1]]))
# #
# # lst=['abc', 'xyz', 'aba', '1221']
# # print(([i for i in lst if len(i)>2 and i[0]==i[-1]]))
# # print(len([i for i in lst if len(i)>2 and i[0]==i[-1]]))
#
# #Write a Python program to get a list, sorted in increasing order by the last element
# # in each tuple from a given list of non-empty tuples
# #
# # lst=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # print(sorted(lst,key=lambda x:x[1]))
# # print(sorted(lst,key=lambda x:x[0]))
#
# #Write a Python program to remove duplicates from a list
# # lst=[10,20,30,20,10,50,60,40,80,50,40]
# # print(sorted(list(set(lst))))
# # unique=[]
# # for i in lst:
# #     if i not in unique:
# #         unique.append(i)
# # print(sorted(unique))
#
# #Write a Python program to check a list is empty or not.
# #
# # def empty(lst):
# #     if len(lst)==0:
# #         return 'empty'
# #     else:
# #         return 'not empty'
# # print(empty([]))
# # print(empty([1,2,3]))
#
# #Write a Python program to clone or copy a list.
# # lst=[1,2,3,4,5,6]
# # lst1=lst[:]
# # print(lst,lst1)
# #
# # lst2=list(lst)
# # print(lst2)
#
# #Write a Python program to find the list of words
# # that are longer than n from a given list of words.
# #
# # def leng(str1,k):
# #     words=str1.split()
# #     return [i for i in words if len(i)>k]
# # print(leng("The quick brown fox jumps over the lazy dog",3))
#
# #Write a Python function that takes two lists and returns True if they have at least
# # one common member.
# #
# # def common(lst1,lst2):
# #     if set(lst1).intersection(set(lst2)):
# #         return ('True')
# #     else:
# #         return ('False')
# #
# # lst1=[1,2,3,4,5]
# # lst2=[6,7,8,9]
# # print(common([1,2,3,4,5],[6,7,8,9,1]))
# # print(common([1,2,3,4,5],[6,7,8,9]))
# # print(common([1,2,3,4,5],[6,7,3,9,1]))
#
# #Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
# # color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # print([v for i,v in enumerate(color) if i not in (0,2,5)])
# #
# # print([(i,v) for i,v in enumerate(color) if i not in (0,2,5)])
#
# # del(color[0])
# # print(color)
#
# # del(color[4])
# # print(color)
# #
# # del(color[5])
# # print(color)
#
# #Write a Python program to generate a 3*4*6 3D array whose each element is *.
# # a=[[[0 for k in range(6)] for j in range(4)] for i in range(3)]
# # print(a)
# #
# # a=[[['*' for k in range(6)] for j in range(4)] for i in range(3)]
# # print(a)
# #
# # a=[[[1 for k in range(3)] for j in range(3)] for i in range(3)]
# # print(a)
#
# #print even and odd numbers from a list
# # num = [7,8, 120, 25, 44, 20, 27]
# # print([i for i in num if i%2==0])
# # print([i for i in num if i%2!=0])
# #
# # #Write a Python program to shuffle and print a specified list.
# # import random
# # num = [7,8, 120, 25, 44, 20, 27]
# # i=0
# # while(i<10):
# #     random.shuffle(num)
# #     print(num)
# #     i+=1
# #
# # #Write a Python program to generate and print a list of first and last 5 elements
# # # where the values are square of numbers between 1 and 30 (both included).
# # print([i**2 for i in range(1,31)])
# # print([i**3 for i in range(1,31)])
# #
# # lst=[]
# # for i in range(1,30):
# #     if i<=5:
# #         lst.append(i)
# #     else:
# #         lst.append(i**2)
# # print(lst)
# #
# # print([i**2 if i>5 else i for i in range(1,30)])
# #
# # l = [22, 13, 45, 50, 98, 69, 43, 44, 1]
# # print([i+1 if i>=45 else i+5 for i in l])
#
# #Write a Python program to generate all permutations of a list in Python.
# # from itertools import permutations
# # lst=[1,2,3,4,5]
# # for p in permutations(lst):
# #     print(list(p))
# #
# # #Write a Python program to get the difference between the two lists.
# # lst1=[1, 3, 5, 7, 9]
# # lst2=[1, 2, 4, 6, 7, 8]
# # # print(set(lst1).difference(set(lst2)))
# # # print(set(lst2).difference(set(lst1)))
# # print(set(lst1).symmetric_difference(set(lst2)))
# # print(set(lst2).symmetric_difference(set(lst1)))
# #
# # #Write a Python program access the index of a list.
# # lst=[1,2,3,4,5,6,7,8,9]
# # for i,v in enumerate(lst):
# #     print(i,v)
# # nums = [5, 15, 35, 8, 98]
# # print([(i,v) for i,v in enumerate(nums)])
#
# #Write a Python program to convert a list of characters into a string.
# # lst=['P','y','t','h','o','n']
# # print(''.join(lst))
#
# #Write a Python program to find the index of an item in a specified list.
# # num = [7,8, 120, 25, 44, 20, 27]
# # print([(i,v) for i,v in enumerate(num) if v%2==0])
# # print([(i,v) for i,v in enumerate(num) if v%2!=0])
# #
# # print(num.index(8))
# # print(num.index(44))
# # print(num.index(25))
#
# #Write a Python program to flatten a shallow list.
# # lst=[[1,2,3],[4,5,6],[7,8,9]]
# # print([lst[j][i] for j in range(3) for i in range(3)])
# #
# # from itertools import chain
# # print(list(chain(*lst)))
# #
# # from itertools import chain
# # lst=[[2,4,3],[1,5,6], [9], [7,9,0]]
# # print(list(chain(*lst)))
#
# #Write a Python program to append a list to the second list.
# # lst1=[1,2,3]
# # lst2=[4,5,6]
# # lst1.extend(lst2)
# # print(lst1)
# #
# # lst1=[1,2,3]
# # lst2=[4,5,6]
# # lst1.append(lst2)
# # print(lst1)
# #
# # lst1=[1,2,3]
# # lst2=[4,5,6]
# # lst2.append(lst1)
# # print(lst2)
# #
# # lst1=[1,2,3]
# # lst2=[4,5,6]
# # lst2.extend(lst1)
# # print(lst2)
# #
# # list1 = [1, 2, 3, 0]
# # list2 = ['Red', 'Green', 'Black']
# # print(list1+list2)
# # list1.extend(list2)
# # print(list1)
#
# #Write a Python program to select an item randomly from a list.
# # import random
# # lst=[1, 2, 3, 0, 'Red', 'Green', 'Black']
# # i=0
# # while(i<10):
# #     print(random.choice(lst))
# #     i+=1
#
# #Write a Python program to find the second smallest number in a list.
# # def second_smallest(lst):
# #     slst=sorted(lst)
# #
# #     if len(slst)>1:
# #         return slst[1],slst[0]
# #     else:
# #         return slst[0]
# # print(second_smallest([1, 2, -8, -2, 0, -2]))
# # print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
# # print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# # print(second_smallest([2,2]))
# # print(second_smallest([2]))
# #
# # #Write a Python program to find the second largest number in a list.
# # def second_largest(lst):
# #     slst=sorted(lst)
# #     if len(slst)>1:
# #         return slst[-2],slst[-1]
# #     else:
# #         return slst[0]
# #
# #
# # print(second_largest([1,2,3,4,4]))
# # print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# # print(second_largest([2,2]))
# # print(second_largest([1]))
#
# #Write a Python program to get unique values from a list.
# # def unique(lst):
# #     unique=[]
# #     dups=[]
# #     # for i in lst:
# #     #     if i not in unique:
# #     #         unique.append(i)
# #     #     else:
# #     #         dups.append(i)
# #     # return unique
# #     return list(set(lst))
# #
# # my_list = [10, 20, 30, 40, 20, 50, 60, 40]
# # print(unique(my_list))
#
# #Write a Python program to get the frequency of the elements in a list.
# # lst=[10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
# # dict1={}
# # for i in lst:
# #     if i not in dict1:
# #         dict1[i]=1
# #     else:
# #         dict1[i]+=1
# # print(dict1)
# # print('number\tcount')
# # for k,v in dict1.items():
# #     print(k,'\t',v)
# #
# # from collections import Counter
# # print(Counter(lst))
# #
# # #Write a Python program to check whether a list contains a sublist.
# # from itertools import permutations
# # lst1=[2,4,3,5,7]
# # lst2=[4,3]
# # lsts=[list(lst) for lst in permutations(lst1,2)]
# # print(lsts)
# # if lst2 in lsts:
# #     print('Yes')
# # else:
# #     print('NO')
#
# #Write a Python program to generate all sublists of a list.
# # from itertools import combinations
# # def sub_lists(lst):
# #     subs=[]
# #     for i in range(0,len(lst)+1):
# #         temp=[list(x) for x in combinations(lst,i)]
# #         if len(temp)>0:
# #             subs.extend(temp)
# #     return subs
# # l1 = [10, 20, 30, 40]
# # l2 = ['X', 'Y', 'Z']
# # print("Original list:")
# # print(l1)
# # print("S")
# # print(sub_lists(l1))
# # print("Sublists of the said list:")
# # print(sub_lists(l1))
# # print("\nOriginal list:")
# # print(l2)
# # print("Sublists of the said list:")
# # print(sub_lists(l2))
# #
# # from itertools import combinations
# # lst=['A','B','C']
# # subs=[]
# # for i in range(0,len(lst)+1):
# #     temp=[list(x) for x in combinations(lst,i)]
# #     subs.extend(temp)
# # print(subs)
#
# # #Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
# # lst1=['p','q']
# # lst2=[str(i) for i in range(1,6)]
# # print(['{}{}'.format(x,y) for y in range(1,6) for x in lst1])
# # lst3=[]
# # for i in lst2:
# #     str1=[]
# #     for j in lst1:
# #         str1=j+i
# #         lst3.append(''.join(str1))
# # print(lst3)
# #Write a Python program to get variable unique identification number or string.
# # a=100
# # c=a
# # b='ab'
# # print(id(a),a)
# # print(id(c),c)
# # print(id(b),b)
#
# #Write a Python program to find common items from two lists.
# # color1 = "Red, Green, Orange, White"
# # color2 = "Black, Green, White, Pink"
# # c1=color1.split(',')
# # c2=color2.split(',')
# # print(set(c1).intersection(set(c2)))
#
# #Write a Python program to change the position of every n-th value with the (n+1)th in a list
#
# #Write a Python program to convert a list of multiple integers into a single integer.
# # lst=[1,2,3,4,5,6,7,8,9]
# # lst=[str(i) for i in lst]
# # a=''.join(lst)
# # b=int(a)
# # print(type(a))
# # print(type(b))
# # print(int(''.join(lst)))
# #
# # #Write a Python program to create multiple lists.
# # print([[] for i in range(10)])
# #
# # print({str(i):[] for i in range(1,21)})
# #
# # #Write a Python program to find missing and additional values in two lists.
# # list1 = ['a','b','c','d','e','f']
# # list2 = ['d','e','f','g','h']
# # print(set(list1).difference(set(list2)))
# # print(set(list2).difference(set(list1)))
#
# #Write a Python program to split a list into different variables.
# # color=['black','red','green']
# # v1,v2,v3=color
# # print(v1)
# # print(v2)
# # print(v3)
#
# #lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# #print([i for i in lst if i%2==0])
# #print([[['*' for column1 in range(6)]for column in range(4)]for row in range(3)])
#
# #Check whether two lists are circularly identical
#
# # def circular(lst1,lst2):
# #     return ' '.join(map(str,lst1)) in ' '.join(map(str,lst2*2))
# #
# #
# # # driver code
# # list1 = [10, 10, 0, 0, 10]
# # list2 = [10, 10, 10, 0, 0]
# # list3 = [1, 10, 10, 0, 0]
# #
# # # check for list 1 and list 2
# # if circular(list1, list2):
# #     print("Yes")
# # else:
# #     print("No")
# #
# # # check for list 2 and list 3
# # if circular(list2, list3):
# #     print("Yes")
# # else:
# #     print("No")
# #Write a Python program to count the number of elements in a list within a specified range.
# #
# # def count_range(lst,min1,max1):
# #     cnt=0
# #     for i in lst:
# #         if min1<=i<=max1:
# #             cnt+=1
# #     return cnt
# # list1 = [10,20,30,40,40,40,70,80,99]
# # print(count_range(list1, 20, 100))
# #
# # def count_range1(lst,min1,max1):
# #     lst1=[]
# #     for i in lst:
# #         if min1<=i<=max1:
# #             lst1.append(i)
# #     return lst1
# # list1 = [10,20,30,40,40,40,70,80,99]
# # print(count_range1(list1, 20, 100))
# #
#
# # class Myclass():
# #
# #     def __init__(self):
# #         self.str1=""
# #
# #     def getstr(self):
# #         self.str1=input()
# #
# #     def putstr(self):
# #         print(self.str1)
# #
# #     def putstr_upper(self):
# #         print(self.str1.upper())
# #
# #     def putstr_reverse(self):
# #         print(self.str1.upper()[::-1])
# #
# # strobj=Myclass()
# # strobj.getstr()
# # strobj.putstr()
# # strobj.putstr_upper()
# # strobj.putstr_reverse()
#
# # str1=input()
# # rowcol=[int(i) for i in str1.split(',')]
# # print(rowcol)
# # row=rowcol[0]
# # col=rowcol[1]
# # multilist=[[0 for c in range(col)] for r in range(row)]
# # print(multilist)
# #
# # for r in range(row):
# #     for c in range(col):
# #         multilist[r][c]=r*c
# # print(multilist)
#
# # lines=[]
# #
# # while True:
# #     s=input()
# #     if s:
# #         lines.append(s.upper())
# #     else:
# #         break
# #
# # print(lines)
# # for i in lines:
# #     print(i)
#
# # import operator
# # lst=[]
# # while True:
# #     s=input()
# #     if s:
# #         lst.append(tuple(s.split(",")))
# #     else:
# #         break
# # print(sorted(lst,key=lambda x:x[0]))
# # print(sorted(lst,key=lambda x:x[1]))
# # print(sorted(lst,key=lambda x:x[2]))
# #
# # print(sorted(lst,key=operator.itemgetter(0)))
# # print(sorted(lst,key=operator.itemgetter(1)))
# # print(sorted(lst,key=operator.itemgetter(2)))
#
# # class Person:
# #
# #     name='Person'
# #
# #     def __init__(self,name=None):
# #         self.name=name
# #
# # jeffrey = Person("Jeffrey")
# # print("%s name is %s" % (Person.name, jeffrey.name))
# #
# # nico = Person()
# # nico.name = "Nico"
# # print("%s name is %s" % (Person.name, nico.name))
#
# # mydict = {'a': [1, 2, 3], 'b': ['one', 'two', 'three']}
# # mydict['a'].append(4)
# # mydict['a'].extend([5,6,7])
# # mydict['b'].append('four')
# # mydict['b'].extend(['five','six'])
# # print(mydict)
#
# # from collections import OrderedDict
# #
# # dict1=OrderedDict()
# #
# # dict1['a']=1
# # dict1['e']=5
# # dict1['b']=2
# # dict1['d']=4
# # dict1['c']=3
# # print(dict1)
# # print(sorted(dict1.items(),key=lambda x:x[0]))
#
# # def family (siddu,santu,shivu):
# #     print('Siddu son is',siddu)
# #     print('Santu son is', santu)
# #     print('Shivu son is', shivu)
# #
# # dict1={'siddu':'Atharv','santu':'Karu','shivu':'Gundya'}
# # print(family(**dict1)) #sending dict key-value pair as keyword arguments
#
# # a=[1,2,3,4]
# # b=[5,6]
# # a.append(b)
# # print(a)
# #
# # a=[1,2,3,4]
# # a.extend([4,5,6])
# # print(a)
#
# # import datetime
# # class Person(object):
# #     def __init__(self, name, birthday, height):
# #         self.name = name
# #         self.birthday = birthday
# #         self.height = height
# #     def __repr__(self):
# #         return self.name
# # l = [Person("John Cena", datetime.date(1992, 9, 12), 175),
# # Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
# # Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]
# # #print(l)
# # l.sort(key=lambda item: item.name)
# # print(l)
# # # l: [Chuck Norris, John Cena, Jon Skeet]
# # l.sort(key=lambda item: item.birthday)
# # # l: [Chuck Norris, Jon Skeet, John Cena]
# # print(l)
# # l.sort(key=lambda item: item.height)
# # # l: [John Cena, Chuck Norris, Jon Skeet]
# # print(l)
# #
# #
# # import datetime
# # l = [{'name':'John Cena', 'birthday': datetime.date(1992, 9, 12),'height': 175},
# # {'name': 'Chuck Norris', 'birthday': datetime.date(1990, 8, 28),'height': 180},
# # {'name': 'Jon Skeet', 'birthday': datetime.date(1991, 7, 6), 'height': 185}]
# # l.sort(key=lambda item: item['name'])
# # # l: [Chuck Norris, John Cena, Jon Skeet]
# # print(l)
# # l.sort(key=lambda item: item['birthday'])
# # # l: [Chuck Norris, Jon Skeet, John Cena]
# # print(l)
# # l.sort(key=lambda item: item['height'])
# # # l: [John Cena, Chuck Norris, Jon Skeet]
# # print(l)
#
#
# # from operator import itemgetter,attrgetter
# # people = [{'name':'chandan','age':20,'salary':2000},
# # {'name':'chetan','age':18,'salary':5000},
# # {'name':'guru','age':30,'salary':3000}]
# # by_age = itemgetter('age')
# # by_salary = itemgetter('salary')
# # people.sort(key=by_age) #in-place sorting by age
# # print(people)
# # people.sort(key=by_salary) #in-place sorting by salary
# # print(people)
# #
# #
# # people = [{'name':'chandan','age':20,'salary':2000},
# # {'name':'chetan','age':18,'salary':5000},
# # {'name':'guru','age':30,'salary':3000}]
# #
# # print(sorted(people,key=lambda x:x['name']))
# # print(sorted(people,key=lambda x:x['age']))
# # print(sorted(people,key=lambda x:x['salary']))
#
# vals = [1, 2, 3, 4]
# print(any(i>12 for i in vals))
# print(any((i*6)>12 for i in vals))
#
# alist = ['a1', 'a2', 'a3']
# blist = ['b1', 'b2', 'b3']
#
# for a,b in zip(alist,blist):
#     print(a,b)
#
# alist = ['a1', 'a2', 'a3','a4']
# blist = ['b1', 'b2', 'b3', 'b4','b5','b6']
# for a,b in zip(alist,blist):
#     print(a,b)
#
# import itertools
#
# alist = ['a1', 'a2', 'a3']
# blist = ['b1']
# clist = ['c1', 'c2', 'c3', 'c4']
#
# for a,b,c in itertools.zip_longest(alist,blist,clist):
#     print(a,b,c)
#
# alist = [123, 'xyz', 'zara', 'abc']
# print(alist)
# alist.insert(3,2021)
# print(alist)
# alist.insert(0,2022)
# print(alist)
#
# names = ["aixk", "duke", "edik", "tofp", "aixk", "duke"]
# print(list(set(names)))
#
# lst = [[[1,2],[3,4]], [[5,6,7],[8,9,10], [12, 13, 14]]]
# print(lst)
#
# lst[0][0].append(11)
# print(lst)
#
# lst[0][1].append(12)
# print(lst)
#
# lst[1][0].append('siddu')
# print(lst)
#
# lst[1][1].append('santu')
# print(lst)
#
# lst[1][2].append('shivu')
# print(lst)
#
# lst=[[[1, 2, 11], [3, 4, 12]], [[5, 6, 7, 'siddu'], [8, 9, 10, 'santu'], [12, 13, 14, 'shivu']]]
# for row in lst:
#     for col in row:
#         print(col)
#
# lst=[[[1, 2, 11], [3, 4, 12]], [[5, 6, 7, 'siddu'], [8, 9, 10, 'santu'], [12, 13, 14, 'shivu']]]
# print(lst[1][1:])
#
# lst=[[[1, 2, 11], [3, 4, 12]], [[5, 6, 7, 'siddu'], [8, 9, 10, 'santu'], [12, 13, 14, 'shivu']]]
#
# print(lst[0][0][0])
# print(lst[0][0][1])
# print(lst[0][0][2])
# print(lst[0][1][0])
# print(lst[0][1][1])
# print(lst[0][1][2])
# print(lst[1][0][0])
# print(lst[1][0][1])
# print(lst[1][0][2])
# print(lst[1][0][3])
# print(lst[1][1][0])
# print(lst[1][1][1])
# print(lst[1][1][2])
# print(lst[1][1][3])
# print(lst[1][2][0])
# print(lst[1][2][1])
# print(lst[1][2][2])
# print(lst[1][2][3])
#
# lst=['None']*10
# print(lst)
#
# lst=['siddu']*10
# print(lst)
#
# lst=[w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']]
# print(lst)
#
# sentence = "Beautiful is better than ugly"
# print([''.join(sorted(word)) for word in sentence.split()])
#
#
# print([x if x in 'aeiou' else '*' for x in 'apple'])
#
# print(''.join([c if c in 'aeiou' else '*' for c in 'siddharooda bagewadi']))
#
# print([sorted(x) for x in [[2, 1], [4, 3], [0, 1]]])
#
# print([x if x%2==0 else 'None' for x in range(20)])
#
# print([x if x>4 else '*' for x in range(10) if x%2==0])
#
# l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
# print([i for x in l for i in x])
#
# print({name:len(name) for name in ('Stack', 'Overflow', 'Exchange') if len(name)>6})
#
# dict1={1: 'a', 2: 'b', 3: 'c'}
# print(dict1)
# print({v:k for k,v in dict1.items()})
#
# dict1 = {'w': 1, 'x': 1}
# dict2 = {'x': 2, 'y': 2, 'z': 2}
#
# dict3={**dict1,**dict2}
# print(dict3)
#
# data = [[1], [2, 3], [4, 5]]
# print([element for eachlist in data if len(eachlist)==2 for element in eachlist if element!=5 ])
#
# print([x**2 for x in range(10)])
# print((x**2 for x in range(10)))
#
# gen=(x**2 for x in range(10))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# #print(next(gen))
# gen=(x**2 for x in range(10))
# for i in range(10):
#     print(next(gen))
#
# print({x for x in range(5)})
#
# text = "When in the Course of human events it becomes necessary for one people..."
# print({ch.lower() for ch in text if ch.isalpha()})
#
# for c in text:
#     if c.isalpha():
#         if c not in dict1:
#             dict1[c]=1
#         else:
#             dict1[c]+=1
# print(dict1)
#
# print([x+y for x,y in [(1, 2), (3, 4), (5, 6)]])
#
# print([x*y for x,y in [(1, 2), (3, 4), (5, 6)]])
#
# # Count the numbers in `range(1000)` that are even and contain the digit `9`:
#
# print([int(x) for x in range(1000) if x%2==0 and '9' in str(x)])
#
# #List Comprehension with nested loop
# print([x+y for x in [1,2,3] for y in [4,5,6]])
#
# #Nested List Comprehension
# print([[x+y for x in [1,2,3]] for y in [4,5,6]])
#
# print([[[i+j+k for k in 'def']for j in 'abc']for i in '123'])
#
# lst=[]
# for i in '123':
#     temp1=[]
#     for j in 'abc':
#         temp2=[]
#         for k in 'def':
#             temp2.append(i+j+k)
#         temp1.append(temp2)
#     lst.append(temp1)
# print(lst)
#
# list_1 = [1, 2, 3 , 4]
# list_2 = ['a', 'b', 'c', 'd']
# list_3 = ['6', '7', '8', '9']
#
# print([(a,b,c) for a,b,c in zip(list_1,list_2,list_3)])
#
# #shifting a list
#
# def shift_list(lst,k):
#     k=k % len(lst)
#     k=k*-1
#     shifted_lst=lst[k:]+lst[:k]
#     return shifted_lst
#
# print(shift_list([1,2,3,4,5],-7))
# print(shift_list([1,2,3,4,5],5))
# print(shift_list([1,2,3,4,5],3))

#identicality of list
# l=[1, 1, 1, 1]
# if len(set(l))==1:
#     print('items identical')
# else:
#     print('not identical')

#Convert Lists into Similar key value lists
# from collections import defaultdict
#
# l1=[5, 6, 6, 6]
# l2=[8, 3, 2, 9]
#
# d=defaultdict(list)
# [d[k].append(v) for k,v in zip(l1,l2)]
# print(d)
#
# d={k:[] for k in l1}
#
# for k,v in zip(l1,l2):
#     d[k].append(v)
# print(d)
#
# l1=[1,2,3]
# l2=[5,6,7]
# print(dict(zip(l1,l2)))

# import collections
# #Write a Python program to find the occurrences of 10 most common words in a given text.
#
# str1='Write a Python program that accept some words and count the number of distinct words. Print the number of ' \
#     'distinct words and number of occurrences for each distinct word according to their appearance.'
# words=str1.split()
# print(collections.Counter(words).most_common(10))

#Write a Python program that accept some words and count the number of distinct words. Print the number of
# distinct words and number of occurrences for each distinct word according to their appearance.
# import collections
#
# words=input().split()
# d=collections.Counter(words)
# print(d)
# occurance=d.values()
# print(occurance)

for i in range(3,16,1):
    si=str(i)
    if len(si)<2:
        print(si)
    elif si[1]==0:
        print(si)