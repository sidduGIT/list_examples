def nested_sum(lst):
    return sum([j for i in lst for j in i])

print(nested_sum([[1,2,3],[4,5,6],[7,8,9]]))

def capitalize(lst):
    return [[j.upper() for j in i] for i in lst ]

print(capitalize([['a','b','c'],['d','e','f'],['g','h','i']]))

def only_upper(lst):
    #return [i for i in lst if i.isupper()]
    return list(filter(lambda x:x.isupper(),lst))

print(only_upper(['abc','DEF','gHI','XYZ','MNO','pqRS']))

def cumulative_sum(lst):
    res=[]
    #res.append(lst[0])
    sum1=0
    for i in range(len(lst)):
        sum1+=lst[i]
        res.append(sum1)
    return res

print(cumulative_sum([1,2,3,4,5,6]))

def middle(lst):
    return lst[1:-1]

print(middle([1,23,4,5,6]))

t=[1,2,3]
x=[4,5,6]
print(t+x)
print(t+[x])
t.append([x])
print(t)

def is_sorted(lst):
    for i in range(len(lst)):
        if lst[i+1]-lst[i]>=0:
            return True
        else:
            return False
            break


print(is_sorted([1,2,3,3,4,4,5]))
print(is_sorted([10,4,3,2,1]))

def anagram(s1,s2):
    s1=''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    print(s1,s2)
    if s1==s2:
        return 'anagram'
    else:
        return 'NOT anagram'

print(anagram('stop','post'))
print(anagram('strip','post'))

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
    c1=Counter(s1)
    c2=Counter(s2)
    if c2-c1==0:
        return True
    else:
        return False

print(is_anagram_counter('abcde','edcba'))
print(is_anagram_counter('heart','earth'))
print(is_anagram_counter('python','typhon'))

def has_duplicates(lst):
    dict1={}
    for i in lst:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
    for k,v in dict1.items():
        if v>1:
            return True
        else:
            return False

print(has_duplicates([1,2,3,1,2,4,5,1,2,3,6,5,7,8,5,2,4,3]))
print(has_duplicates([1,2,3,4,5]))

def dups(lst):
    unique=[]
    dupls=[]
    for i in lst:
        if i not in unique:
            unique.append(i)
        else:
            dupls.append(i)
    return unique,dupls

print(dups([1,2,3,4,5,6,7,1,2,3,2,4,5,3,1]))

import time
def make_word_list1():
    lst1=[]
    with open('words.txt','r') as fr:
        for line in fr:
            word=line.strip()
            lst1.append(word)
    return lst1
def make_word_list2():
    lst2=[]
    with open('words.txt','r') as fr:
        for line in fr:
            word=line.strip()
            lst2=lst2+[word]
    return lst2

start_time=time.time()
t=make_word_list1()
end_time=time.time()
print(len(t))
print(t[:10])
print('total time in seconds for list1',end_time-start_time)

start_time=time.time()
t=make_word_list2()
end_time=time.time()
print(len(t))
print(t[:10])
print('total time in seconds for list2',end_time-start_time)

with open('words.txt','r') as fr:
    for line in fr:
        word=line.strip()
        if word==word[::-1]:
            print(word)

def new_word(word1,word2):
    new_word=[]
    for ch1,ch2 in zip(word1,word2):
        new_word.append(ch1)
        new_word.append(ch2)
    return ''.join(new_word)

print(new_word('shoe','cold'))

with open('words.txt','r') as fr:
    dict1={}
    for line in fr:
        word=line.strip()
        dict1[word]=1
    if 'aal' in dict1:
        print('True')
    else:
        print('False')
print(dict1)

