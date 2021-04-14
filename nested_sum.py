def nested_sum(lst):
    sum1=0
    # for sublst in lst:
    #     sum1+=sum(sublst)
    # return sum1

    for i in lst:
        for j in i:
            sum1+=j
    return sum1

print(nested_sum([[1,2,3],[4,5,6],[7,8,9],[10,11]]))


def nested_capital(lst):
    res=[]
    for i in lst:
        sublist=[]
        for j in i:
            sublist.append(j.upper())
        res.append(sublist)
    return res

print(nested_capital([['a','b','c'],['d','e','f'],['g','h']]))


def cumulative_sum(lst):
    res=[]
    res.append(lst[0])
    for i in range(0,len(lst)-1):
        res.append(res[i]+lst[i+1])
    return res

print(cumulative_sum([1,2,3,4,5,6,7,8]))

lst=['a','b','C','D','e','F','G','h','i','J']
print([i for i in lst if i.isupper()])

def upper(c):
    if c.isupper():
        return True
    else:
        return False
lst=['a','b','C','D','e','F','G','h','i','J']
print(list(filter(lambda x:x.isupper(),lst)))

my_list = ["geeks", "geeg", "keek", "practice", "aa"]
print([i for i in my_list if i==i[::-1]])

def caps(lst):
    res=[]
    for i in lst:
        sublist=[]
        for j in i:
            res.append(j.upper())
    return res

def caps1(lst):
    return [[j.upper() for j in i] for i in lst ]

print(caps1([['abc','def'],['ghi','jkl','mno'],['pqrs']]))

def middle(lst):
    return lst[1:-1]

print(middle([1,2,3,4,5]))
print(middle([1,2,3]))


def is_sorted(lst):
    for i in range(0,len(lst)-1):
        if lst[i+1]-lst[i]==-1:
            return True
        else:
            return False

#print(is_sorted([1,2,3,4,5,]))
print(is_sorted([5,4,3,2,1]))

def is_anagram(s1,s2):
    s1=''.join(sorted(s1))
    s2=''.join(sorted(s2))
    if s1==s2:
        return True
    else:
        return False

print(is_anagram('abc','cab'))
print(is_anagram('abc','cad'))

def duplicate(lst):
    dups=[]
    nondups=[]
    for i in lst:
        if i in dups:
            nondups.append(i)
        else:
            dups.append(i)
    return dups

print(duplicate([1,2,1,2,3,4,5,4,2,5,2,1,5]))

