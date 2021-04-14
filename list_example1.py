#Python program to find a series in an array consisting of characters
# def find_series(lst):
#     for i in range(0,len(lst)-2):
#         if lst[i]=='a' and lst[i+1]=='b' and lst[i+2]=='c':
#             return True
#     return False
#
# print(find_series(['a', 'x', 'a', 'b', 'c']))
# print(find_series(['f', 'x', 'a', 'i', 'c', 't']))
# print(find_series(['k', 'x', 'a', 'e', 'c']))
#
# #matrix operations
# mat = [
#   [10, 20, 30],
#   [40, 50, 60],
#   [70, 80, 80]
# ]
#
# for i in range(len(mat)):
#     print(mat[i])
#
# for i in range(len(mat)):
#     for j in range(len(mat)):
#         print(mat[i][j])
# print([mat[i][j] for j in range(len(mat)) for i in range(len(mat))])
#
# mat1=[
#   [10, 20, 30],
#   [40, 50, 60],
#   [70, 80, 90]
# ]
#
# mat2=[
#   [10, 20, 30],
#   [40, 50, 60],
#   [70, 80, 90]
# ]
#
# #mat3=[0 for j in range(len(mat1)) for i in range(len(mat1))]
# # print(mat3)
# mat3=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(mat3)):
#     for j in range(len(mat3)):
#         mat3[i][j]=mat1[i][j]+mat2[i][j]
# print(mat3)
#
# mat3=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(mat3)):
#     for j in range(len(mat3)):
#         mat3[i][j]=mat1[i][j]*mat2[i][j]
# print(mat3)
#
# mat3=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(mat3)):
#     for j in range(len(mat3)):
#         mat3[i][j]=mat1[i][j]//mat2[i][j]
# print(mat3)
#
# mat3=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(mat3)):
#     for j in range(len(mat3)):
#         mat3[i][j]=mat1[i][j]-mat2[i][j]
# print(mat3)

# str1 = "Hello World How are you?"
# words=str1.split()
# dict1={}
# for word in words:
#     dict1[word]=len(word)
# print(dict1)
#
# lengs=[len(word) for word in words]
# print(dict(zip(lengs,words)))

#Check if a substring presents in a string using 'in' operator

# str1='substring'
# if 'sub' in str1:
#     print('Yes')
# if 'string' in str1:
#     print('Yes')

#substrings of a string

#str1='substring'
# str1='gadag'
# n=len(str1)
# substr=[]
# for i in range(n):
#     for j in range(i,n):
#         substr.append(str1[i:j])
# print(substr)
#
# for pali in substr:
#     if pali==pali[::-1]:
#         print(pali)

# str1='substring'
# leng=len(str1)-1
# rev=''
# while leng>=0:
#     rev+=str1[leng]
#     leng-=1
# print(rev,rev[::-1])

# str1='gadag'
# i=0
# j=len(str1)-1
# flag=0
# while j>=0:
#     if str1[i]==str1[j]:
#         flag=1
#     else:
#         flag=0
#         break
#     i+=1
#     j-=1
# print(flag)

# from itertools import combinations
# lst=[1,4,20,3,10,5]
# sum1=33
# indices=[]
# for i in range(len(lst)):
#     for combi in combinations(lst,i):
#         if sum(combi)==sum1:
#             for j in combi:
#                 indices.append(lst.index(j))
# print(indices)

# lst=[1,4,20,3,10,5,18,10]
# sum1=33
# nums=[]
# indices=[]
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         for k in range(j+1,len(lst)):
#             if lst[i]+lst[j]+lst[k]==sum1:
#                 nums.append((lst[i],lst[j],lst[k]))
#                 indices.append((i,j,k))
# print(nums,indices)

# s='siddu'
# permut=[]
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         permut.append(s[i:j])
# print(permut)
#
# from itertools import permutations
# for combi in permutations(s,2):
#     print(combi)

# for i in [2,3,4,0,5,6,7,8]:
#     print(100//i)

# try:
#     for i in [2,3,4,0,5,6,7,8]:
#         print(100//i)
# except ZeroDivisionError:
#     print('contrl has come here')

# gcd function
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n

class Fraction:

    def __init__(self,top,bottom):
        self.num=top
        self.den=bottom

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def __str__(self):
        return str(self.num)+'/'+str(self.den)

    def show(self):
        return str(self.num)+'/'+str(self.den)

    def __add__(self, other_fraction):
        new_num=self.num * other_fraction.den + \
                self.den * other_fraction.num
        new_den=self.den * other_fraction.den
        common=gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other_fraction):
        new_num=self.num * other_fraction.den - \
                self.den * other_fraction.num
        new_den=self.den * other_fraction.den
        common=gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __mul__(self, other_fraction):
        new_num=self.num * other_fraction.den * \
                self.den * other_fraction.num
        new_den=self.den * other_fraction.den
        common=gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num


f1=Fraction(3,5)
print(f1.__str__())
print(f1.show())

f1=Fraction(1,2)
f2=Fraction(1,2)
print(f1+f2)

print(f1-f2)

print(f1*f2)

print(f1==f2)

f1=Fraction(1,2)
f2=Fraction(1,4)
print(f1+f2)

print(f1-f2)

print(f1*f2)

print(f1==f2)

def is_anagram(s1,s2):
    lst1=sorted(s1)
    lst2 = sorted(s2)
    pos=0
    matches=True
    while pos<len(lst1) and matches:
        if lst1[pos]==lst2[pos]:
            pos=pos+1
        else:
            matches=False
    return matches

print(is_anagram('abcde','edcba'))
print(is_anagram('heart','earth'))
print(is_anagram('python','typhon'))

from collections import Counter
def is_anagram_counter(s1,s2):
    c1=set(s1)
    c2=set(s2)
    print(c2,c1,c2-c1)
    if c2-c1==set():
        return True
    else:
        return False

print(is_anagram_counter('abcde','edcba'))
print(is_anagram_counter('heart','earth'))
print(is_anagram_counter('python','typhon'))

def anagram_sol(s1,s2):
    c1=[0]*26
    c2=[0]*26
    for i in range(len(s1)):
        pos=ord(s1[i])-ord('a')
        c1[pos]=c1[pos]+1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j=0
    matches=True
    while j<26 and matches:
        if c1[j]==c2[j]:
            j=j+1
        else:
            matches=False
    return matches

print(anagram_sol('abcde','edcba'))
print(anagram_sol('heart','earth'))
print(anagram_sol('python','typhon'))









