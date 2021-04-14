#Write a Python program to sum all the items in a list
lst=[1,2,3,4,5,6,7,8,9]
sum=0
for i in lst:
    sum+=i
print('sum of list items',sum)

#Write a Python program to multiplies all the items in a list.

lst=[1,2,3,4,5,6,7,8,9]
nlst=[]
for i in lst:
    nlst.append(i*5)
print('sum of list items',nlst)

def prod_list(lst):
    prod=1
    for i in lst:
        prod=prod*i
    return prod

print(prod_list([1,2,3,4,5,6]))

#Write a Python program to get the largest number from a list.
def big_list(lst):
    big=lst[0]
    for i in lst:
        if i>big:
            big=i
    return big
print('big number within a list',big_list([1,2,3,40,5,6]))

def small_list(lst):
    small=lst[0]
    for i in lst:
        if i<small:
            small=i
    return small
print('small number within a list',small_list([1,2,-3,40,5,6]))

#Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings
def count_str(lst):
    count=0
    for item in lst:
        if len(item)>=2 and item[0]==item[-1]:
            count+=1
    return count
print(count_str(['abc', 'xyz', 'aba', '1221','11','aa']))

#Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
from operator import itemgetter
lst=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print('sorting on second item',sorted(lst,key=itemgetter(1)))

print('sorting on second item',sorted(lst,key=lambda x:x[1]))

print('sorting on first item',sorted(lst,key=lambda x:x[0]))

print('sorting on first item',sorted(lst,key=itemgetter(0)))

def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#. Write a Python program to remove duplicates from a list.

def remove_duplicates(lst):
    nlst=[]
    for item in lst:
        if item not in nlst:
            nlst.append(item)
    return nlst

print('list after removing duplicates',remove_duplicates([1,2,-3,-3,4,5,6,2,4,8,9]))

#Write a Python program to check a list is empty or not.

def check_empty(lst):
    flag=0
    if len(lst)==0:
        flag=1
    else:
        flag = 0
    return flag
if check_empty([1]):
    print('list is empty')
else:
    print('list is NOT empty')

l = []
if not l:
  print("List is empty")

import copy
#Write a Python program to clone or copy a list.
lst1=[1,2,-3,-3,4,5,6,2,4,8,9]
lst2=copy.copy(lst1)
print(lst2)

lst2=copy.deepcopy(lst1)
print(lst2)

lst2=list(lst1)
print(lst2)

#Write a Python program to find the list of words that are longer than n from a given list of words
def long_list(lst,n):
    nlst=[]
    for item in lst:
        if len(item)>n:
           nlst.append(item)
           nlst.append(' ')
    return ''.join(nlst)

print(long_list(['siddu','santu','Atharv','surabhi','baba','kaka'],5))

def long_list(str1,n):
    nlst=[]
    for item in str1.split(' '):
        if len(item)>n:
           nlst.append(item)
           nlst.append(' ')
    return ''.join(nlst)

print(long_list("The quick brown fox jumps over the lazy dog",3))

#Write a Python function that takes two lists and returns True if they have at least one common member.
def compare_list(list1,list2):
    result=False
    for item1 in list1:
        for item2 in list2:
            if item1==item2:
                result=True
                return result

print(compare_list([1,2,3],[4,1,6]))
print(compare_list([1,2,3],[4,5,6]))

print(compare_list([1,2,3,4,5], [5,6,7,8,9]))
print(compare_list([1,2,3,4,5], [6,7,8,9]))

#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
def remove_index(lst1,n):
    index=0
    nlst=[]
    for item in lst1:
        if index==n:
            pass
        else:
            nlst.append(item)
        index += 1
    return nlst
print(remove_index(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'],0))
print(remove_index(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'],3))
print(remove_index(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'],5))

#Write a Python program to generate a 2*3 2D array whose each element is *.

array=[[ '*' for col in range(3)]for row in range(2)]
print(array)

array=[[ '*' for col in range(2)]for row in range(3)]
print(array)

array=[[ '*' for col in range(3)]for row in range(3)]
print(array)

for row in range(3):
    for col in range(3):
        array[row][col]='1'
print(array)

#create 3X3 array with element 1234..

for row in range(3):
    for col in range(3):
        array[row][col]=col
print(array)

for row in range(3):
    for col in range(3):
        array[row][col]=row
print(array)

#Write a Python program to print the numbers of a specified list after removing even numbers from it

def even_odd_list(lst):
    # nlst=[]
    # for i in lst:
    #     if i%2==0:
    #         pass
    #     else:
    #         nlst.append(i)
    lst=[i for i in lst if i%2==0]
    return lst

    #lst = [i for i in lst if i % 2 != 0]
    #return lst
print(even_odd_list([1,2,3,4,5,6,7,8,9,10,11,12]))

#Write a Python program to shuffle and print a specified list.

from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

dice=[1,2,3,4,5,6]
for i in range(20):
    shuffle(dice)
    print(dice[0])
# Write a Python program to generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30 (both included)
lst=[]
for i in range(1,31):
    lst.append(i**2)
print('first 5 elements',lst[:5])
print('last five elements',lst[-5:])

#Write a Python program to generate and print a list except for the first 5 elements,
# where the values are square of numbers between 1 and 30 (both included).
lst=[]
for i in range(1,31):
    lst.append(i**2)
print('after removing first 5 elements',lst[5:])

#Write a Python program to generate all permutations of a list in Python.
import itertools
print(list(itertools.permutations([1,2,3])))

import itertools
print(list(itertools.permutations(['A','B','C'])))

#Write a Python program to get the difference between the two lists.
list1 = [1, 2, 3, 4]
list2 = [1, 2,5,6]

print(set(list1))
print(set(list2))

list3=list(set(list1)-set(list2))
print(list3)

list3=list(set(list2)-set(list1))
print(list3)

def list_difference(lst1,lst2):
    lst3=[]
    for i in lst1+lst2:
        if i not in lst1 or i not in lst2:
            lst3.append(i)
    return lst3
li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35,50]
li3 = list_difference(li1, li2)
print(li3)

#Write a Python program access the index of a list
lst= [10, 15, 20, 25, 30, 35, 40]
index=0
dict1={}
for i in lst:
    dict1[i]=index
    index += 1
print('Value',' ','Index')
for index,value in dict1.items():
    print(index,'   ',value)

lst= [10, 15, 20, 25, 30, 35, 40]
for index,value in enumerate(lst):
    print(index,value)

#Write a Python program to convert a list of characters into a string
lst=['s','i','d','d','u']
nlst=[]
for i in lst:
    nlst.append(i)
print('after converting chars into strings','"',''.join(nlst),'"')

# Write a Python program to find the index of an item in a specified list.
def find_index(lst,num):
    index=0
    for item in lst:
        if item==num:
            return index
        index+=1
print('the index of specified number is',find_index([10, 15, 20, 25, 30, 35, 40],10))
print('the index of specified number is',find_index([10, 15, 20, 25, 30, 35, 40],25))
print('the index of specified number is',find_index([10, 15, 20, 25, 30, 35, 40],40))

num =[10, 30, 4, -6]
print(num.index(30))

#Write a Python program to append a list to the second list.
lst1=[10,20,30]
lst2=[40,50,60]
lst2.append(lst1)
print(lst2)

list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list)

#Write a Python program to select an item randomly from a list.
import random
lst= [10, 15, 20, 25, 30, 35, 40]
print('randomly selecting list value',random.choice(lst))

#Write a Python program to flatten a shallow list.

original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
nlst=[]
for item in original_list:
    for i in item:
        nlst.append(i)
print('flattened list is',nlst)

import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_merged_list = list(itertools.chain(*original_list))
print(new_merged_list)

#Write a Python program to find the second smallest number in a list.

lst=[2, 4, 3, 1, 5, 6, 9, 7, 9, 0]
print("original list",lst)
set_lst=set(lst) #set to remove duplicates
print('list after using set',set_lst)
nlst=sorted(set_lst)
print('first smallest number',nlst[0])
print('second smallest number',nlst[1])

print('first biggest number',nlst[-1])
print('second biggest number',nlst[-2])

#Write a Python program to get unique values from a list.
lst=[2, 4, 3, 1, 5, 6, 9, 7, 9, 0,1,5]
unique_list=[]
for i in lst:
    if i not in unique_list:
        unique_list.append(i)
print('unique list is',unique_list)

#Write a Python program to get the frequency of the elements in a list.
#lst=[2, 4, 3, 1, 5, 6, 9, 7, 9, 0,1,5]
lst=[10,10,10,10,20,20,20,20,40,40,50,50,30]

dict1={}
for i in lst:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+= 1
print('Value',' ','Frequency')
for value,freq in dict1.items():
    print(value,'   ',freq)

#Write a Python program to count the number of elements in a list within a specified range
#lst=[10,20,30,40,40,40,70,80,99]
#lst=[10,20,30,40,70,80,99]
lst= ['a','b','c','d','e','f']
range1='a'
range2='f'
count=0
for item in lst:
    if item>range1 and item<range2:
        count+=1
print('number of items within specified range',count)

def count_range_in_list(li, min, max):
	ctr = 0
	for x in li:
		if min <= x <= max:
			ctr += 1
	return ctr

list1 = [10,20,30,40,40,40,70,80,99]
print(count_range_in_list(list1, 40, 100))

list2 = ['a','b','c','d','e','f']
print(count_range_in_list(list2, 'a', 'e'))

#Write a Python program to check whether a list contains a sublist.

def is_Sublist(lst,sublst):
    sub_set=False
    if sublst==[]:
        sub_set=True
    elif sublst==lst:
        sub_set = True
    elif len(sublst)>len(lst):
        sub_set=False
    else:
        for i in range(len(lst)):
            if lst[i]==sublst[0]:
                n=1
                while(n<len(sublst)) and (lst[i+n]==sublst[n]):
                    n+=1
                if n==len(sublst):
                    sub_set=True
    return sub_set

a = [2,4,3,5,7]
b = [4,5]
c = [3,5]
print(is_Sublist(a, b))
print(is_Sublist(a, c))

#Write a Python program to generate all sublists of a list.

def generate_sublist(lst):
    sublists=[[]]
    # for i in range(len(lst)):
    #     n=i+1
    #     while(n<=len(lst)):
    #         sub=lst[i:n]
    #         sublists.append(sub)
    #         n+=1
    for i in range(len(lst)+1):
        for j in range(i+1,len(lst)+1):
            sublist=lst[i:j]
            sublists.append(sublist)
    return sublists

l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
print(generate_sublist(l1))
print(generate_sublist(l2))
#Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
# n=10
# lst=[1,2]
# nlst=[]
# for i in range(1,n+1):
#     nlst.append(lst[0]+i)
#     nlst.append(lst[1] + i)
# print(nlst)

#my_list = ['p', 'q']
my_list = [1, 2]
n = 4
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)

#Write a Python program to get variable unique identification number or string.
x_int=10
print(id(x_int))
print(id(x_int))
x_str='siddu'
print(id(x_str))
x_float=4.0
print(id(x_float))
x_char='s'
print(id(x_char))

#Write a Python program to find common items from two lists
lst1=[1,2,3,4]
lst2=[6,7,8,9]
print(set(lst1))
print(set(lst2))
print(set(lst1)&set(lst2))

#Write a Python program to change the position of every n-th value with the (n+1)th in a list
from itertools import zip_longest, chain, tee
def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n = [0,1,2,3,4,5]
print(replace2copy(n))

#Write a Python program to convert a list of multiple integers into a single integer
L = [11, 33, 50]
print("Original List: ",L)
x = int("".join(map(str, L)))
print("Single Integer: ",x)

#Write a Python program to create multiple lists.
list_of_lists=[]
for i in range(1,21):
    list_of_lists.append(i)
    list_of_lists.append('[]')
print(list_of_lists)

list_of_dicts=[]
for i in range(1,21):
    #list_of_dicts.append(i)
    list_of_dicts.append({})
print(list_of_dicts)

dict_of_lists={}
for i in range(1,21):
    dict_of_lists[i]=[]
print(dict_of_lists)

obj = {}
for i in range(1, 21):
    obj[str(i)] = []
print(obj)

#Write a Python program to find missing and additional values in two lists.
lst1=['a','b','c','d','e']
lst2=['e','f','g','d','h']
extra_values_lst2=[]
extra_values_lst1=[]
for i in lst1:
    if i not in lst2:
        extra_values_lst1.append(i)
print('extra values in list1',extra_values_lst1)

for i in lst2:
    if i not in lst1:
        extra_values_lst2.append(i)
print('extra values in list2',extra_values_lst2)

#Write a Python program to split a list into different variables.
color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
# var1, var2, var3 = color
# print(var1)
# print(var2)
# print(var3)
#
for i in range(len(color)):
    print(color[i][0])

for i in range(len(color)):
    print(color[i][1])

for i in range(len(color)):
    print(color[i][2])
single_list=[]
for i in range(len(color)):
    for j in range(len(color)):
        print('extracting each element',color[i][j])
        single_list.append(color[i][j])
print('single list',single_list)

#Write a Python program to generate groups of five consecutive numbers in a list.
lists=[]
for i in range(5):
    sub = []
    for j in range(1, 6):
        sub.append(5*i+j)
    lists.append(sub)
print(lists)

l = [[5*i + j for j in range(1,6)] for i in range(5)]
print(l)

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
L=set().union(*L)
print(L)
print(sorted(L))

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]
print("Original List: ", L)
print("Sorted Unique Data:",sorted(set().union(*L)))

#Write a Python program to select the odd items of a list.
lst=[1,2,3,4,5,6,7,8,9,10]
olst=[i for i in lst if i%2!=0]
elst=[i for i in lst if i%2==0]
print('odd list',olst)
print('even list',elst)

#Write a Python program to insert an element before each element of a list.
lst=[1,2,3,4,5,6,7,8,9,10]
element=8
nlst=[]
for i in lst:
    nlst.append(element)
    nlst.append(i)
print('after inserting element in each items',nlst)

color = ['Red', 'Green', 'Black']
print("Original List: ",color)
color=[x for i in color for x in ('10',i)]
print("Modified List: ",color)

#Write a Python program to print a nested lists (each list on a new line) using the print() function.

print('\n'.join(str(item)for item in [['red'],['black'],['white'],['purple']]))

colors = [['Red'], ['Green'], ['Black']]
print('\n'.join([str(lst) for lst in colors]))

#Write a Python program to convert list to list of dictionaries.
lst1=["Black", "Red", "Maroon", "Yellow"]
lst2=["#000000", "#FF0000", "#800000", "#FFFF00"]
#nlst=[{'color_name':x,'color_code':y} for x,y in zip(lst1,lst2)]
#print(nlst)
nlst=[]
for x,y in zip(lst1,lst2):
    nlst.append({'color_name':x,'color_code':y})
print(nlst)
nlst1_dict=[]
nlst2_dict=[]
for i in lst1:
    nlst1_dict.append({'color':i})

for i in lst2:
    nlst2_dict.append({'code':i})
print(nlst1_dict)
print(nlst2_dict)

#Write a Python program to sort a list of nested dictionaries
from operator import itemgetter
# lst=[[8,4],[7,1],[9,2],[10,3]]
# print(sorted(lst,key=itemgetter(1)))
# print(sorted(lst,key=itemgetter(0)))

my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print("Original List: ")
print(my_list)
my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
print("Sorted List: ")
print(my_list)

my_list = [{'key': 1}, {'key': 10}, {'key': 5},{'key': 4},{'key': 2}]
print(sorted(my_list,key=itemgetter('key')))

#Write a Python program to split a list every Nth element
#Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
#Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

lst=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
step=4
nlst=[]
for i in range(step):
    nlst.append(lst[i::step])
print(nlst)

lst=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
step=3
nlst=[]
nlst.append(lst[0:step])
nlst.append(lst[step:step*2])
nlst.append(lst[step*2:step*3])
nlst.append(lst[step*3:step*4])
nlst.append(lst[step*4:step*5])
print(nlst)

#Write a Python program to compute the similarity between two lists
#Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
#Expected Output:
#Color1-Color2: ['white', 'orange', 'red']
#Color2-Color1: ['black', 'yellow']

lst1=["red", "orange", "green", "blue", "white"]
lst2=["black", "yellow", "green", "blue"]
print(list(set(lst1)-set(lst2)))

print(list(set(lst2)-set(lst1)))
from collections import Counter
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
counter1 = Counter(color1)
counter2 = Counter(color2)
print(counter1-counter2)
print(counter2-counter1)
print("Color1-Color2: ",list(counter1 - counter2))
print("Color2-Color1: ",list(counter2 - counter1))

#Write a Python program to create a list with infinite elements
import itertools
lst=[]
c=itertools.count()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
for i in range(100):
    lst.append(next(c))
print(lst)

#Write a Python program to concatenate elements of a list with '-'
lst1=[1,2,3,4,5,6,7]
lst2=[]
for i in lst1:
    lst2.append(str(i))
print('-'.join(lst2))

color = ['red', 'green', 'orange']
print('-'.join(color))

#Write a Python program to remove key values pairs from a list of dictionaries.
lst=[{'a':1},{'b':2},{'a':3},{'d':4},{'e':5}]
print(lst)
del(lst[0])
print(lst)

original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]
print(original_list)

new_list=[{k:v for k,v in dict1.items() if k!='key1'} for dict1 in original_list]
print(new_list)

lst=[{'a':1},{'b':2},{'a':3},{'d':4},{'e':5}]
new_lst=[{k:v for k,v in dict1.items() if k!='a'} for dict1 in lst]
print(new_lst)

#Write a Python program to convert a string to a list.
str1="siddu bagewadi"
lst=[]
for char in str1:
    if char==' ':
        pass
    else:
        lst.append(char)
print(lst)

import ast
color ="['Red', 'Green', 'White']"
print('before converting to string',color)
print('after converting to string',ast.literal_eval(color))

#Write a Python program to check if all items of a list is equal to a given string
# lst=['s', 'i', 'd', 'd', 'u',' ', 'b', 'a', 'g', 'e', 'w', 'a', 'd', 'i']
# str2=''.join(lst)
# str1='siddu bagewadi'
# if (set(str1)-set(str2)):
#     print('string and list are equal')
# else:
#     print('string and list are NOT equal')

color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]
check='green'
flag=0
for str1 in color2:
    if str1==check:
        flag=1
    else:
        flag=0
if flag:
    print('all entries of list are equal to given string')
else:
    print('all entries of list are NOT equal to given string')

#Write a Python program to replace the last element in a list with another list.
#Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
#Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

lst1=[1, 3, 5, 7, 9, 10]
lst2=[2, 4, 6, 8]
lst3=lst1[0:len(lst1)-1]
for i in lst2:
    lst3.append(i)
print(lst3)

lst1[-1:]=lst2
print(lst1)

#Write a Python program to split a list based on first character of word.
from itertools import groupby
from operator import itemgetter

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
# dict1={}
# for word in word_list:
#     dict1[word[0]]=word
#
# print(dict1)

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)
#Write a Python program to check if the n-th element exists in a given list.
lst=[1,2,3,4,5,6,7,8,9,10,11,12]
index=100
try:
    if lst.index(index):
        print('nth element exist')
        print('nth element',lst[index])

except ValueError:
    print('nth element NOT exist')

x = [1, 2, 3, 4, 5, 6]
xlen = len(x)-1
print(x[xlen])

#Write a Python program to find a tuple, the smallest second index value from a list of tuples.
lst=[(5,6),(3,4),(1,2),(7,8)]
print(sorted(lst))

#Write a Python program to create a list of empty dictionaries.
lst=[{} for i in range(10)]
print('list of empty dictionaries',lst)

lst=[() for i in range(10)]
print('list of empty tuples',lst)

lst=[[] for i in range(10)]
print('list of empty lists',lst)

dict1={}
for i in range(10):
    dict1[i]=[]
print('dictionary of empty lists',dict1)

dict1={}
for i in range(10):
    dict1[i]=()
print('dictionary of empty tuples',dict1)

dict1={}
for i in range(10):
    dict1[i]={}
print('dictionary of empty dictionaries',dict1)

tup1=[[] for i in range(10)]
print('tuple of empty lists',tuple(tup1))

tup1=[{} for i in range(10)]
print('tuple of empty dictionaries',tuple(tup1))

tup1=[() for i in range(10)]
print('tuple of empty tuples',tuple(tup1))

#Write a Python program to print a list of space-separated elements.
lst=[1,2,3,4,5,6]
print('with , output',lst)
print('without , output',*lst)

a,*b,c=lst
print(a)
print(b)
print(c)

#Write a Python program to insert a given string at the beginning of all items in a list.
lst=[1,2,3,4,5,6,7]
str1='siddu'
lst=[str1+str(i) for i in lst]
print(lst)

lst=[1,2,3,4,5,6,7]
print(['emp{0}'.format(i) for i in lst])

#Write a Python program to iterate over two lists simultaneously.
lst1=[1,2,3,4,5]
lst2=['siddu','santu','shiva','atharv','surabhi']

for l1,l2 in zip(lst1,lst2):
    print(l1,l2)

#Write a Python program to access dictionary key’s element by index.
num = {'physics': 80, 'math': 90, 'chemistry': 86}
for key1 in num.keys():
    print(key1)
keys=list(num.keys())
print(keys[0])
print(keys[1])
print(keys[2])

num = {'physics': 80, 'math': 90, 'chemistry': 86}
print(list(num)[0])
print(list(num)[1])
print(list(num)[2])
for i in range(len(num)):
    print(list(num)[i])

#Write a Python program to find the list in a list of lists whose sum of elements is the highest.
lsts=[[1,2,3], [4,5,6], [10,11,12], [7,8,9],[20,21,22]]
sum1=sum(lsts[0])
for lst in lsts:
    if sum(lst)>sum1:
        sum1=sum(lst)
        big_list=lst
        sum_big=sum(big_list)
print('Big list is {} and its sum are {}'.format(big_list,sum_big))

num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
print(max(num))

#Write a Python program to find all the values in a list are greater than a specified number
lst=[23,45,67,12,78,49,54,63]
num=45
nlst=[]
for i in lst:
    if i>num:
        nlst.append(i)
print(nlst)

list1 = [220, 330, 500]
list2 = [12, 17, 21]
print(all(x>=200 for x in list1))
print(all(x>=25 for x in list2))

#Write a Python program to extend a list without append.
lst1=[10, 20, 30]
lst2=[40, 50, 60]
print(lst2+lst1)
print(lst1+lst2)
#print(list(lst1.extend(lst2)))

lst1[:0]=lst2
print(lst1)

lst1[0:]=lst2
print(lst1)

#Write a Python program to remove duplicates from a list of lists.

from itertools import groupby
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Original List", num)
num.sort()
new_num = list(num for num,group in groupby(num))
print("New List", new_num)

#Write a Python program to get the depth of a dictionary.
def depth(dict1):
    count=0
    str_dict1=str(dict1)
    for i in str_dict1:
        if i=='{':
           count+=1
    return count
dict1 = {1:'Geek', 2: {3: {4: {}}}}
print(depth(dict1))

# 2: Using recursion
def recurse_depth(dict1):
    if isinstance(dict1,dict):
        return 1+(max(map(recurse_depth,dict1.values())) if dict1 else 0)
    return 0
# Driver code
my_dict = {1:'a', 2: {3: {4: {5:{6:{}}}}}}
print(recurse_depth(my_dict))

#Write a Python program to check if all dictionaries in a list are empty or not.
lst1=[{},{},{}]
lst2=[{1,2},{},{}]
flag=0
for i in lst2:
    if len(i):
        #print(len(i))
        flag=1
    else:
        flag=0
if flag:
    print('all dictionary items in a list are NOT empty')
else:
    print('all dictionary items in a list are empty')

# lst1=[{},{},{}]
# for d in lst1:
#     if len(d):
#         print(len(d))
#     else:
#         print('nothing')
my_list = [{},{},{}]
my_list1 = [{1,2},{},{}]
print(all(not d for d in my_list))
print(all(not d for d in my_list1))