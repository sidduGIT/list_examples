items=[2.2,"pam",4+3j,"andy",4]
items[2]="complex"
items.append("dell")
items.insert(0,"bangalore")
print items

value=items.pop(-3)
print value
print
print items

del items[0],items[1]
print items

items=[2.2,"pam",4+3j,"andy",4]
items.remove("pam")
print items

items=[2.2,"pam",4+3j,"andy",4]
items3=items*3
print items3

print
print

item=4+3j
while item in items3:
    items3.remove(item)
print items3

