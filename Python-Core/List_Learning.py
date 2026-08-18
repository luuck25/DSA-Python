
# how to create list
a = [1,2,3]


ab = list((1,2,3))

lst = list('hello')

lst1 = list(range(5))

#From Another List

lst = ab.copy()
lst = ab[:]
lst = list(ab)

# list from Set
list_set = list({1,2,3})

# list from Dict - Keys

sample_dict = {"a":1,"b":2}
#list_dict = list({"a":1,"b":2}) #keys only

listkeys = list(sample_dict.keys())

listvalues = list(sample_dict.values())

print(listkeys)
print(listvalues)

"""
Get Both Key and Value

Use .items(). """

lst = list(sample_dict.items())
print(lst)


#Output:

[('a', 1), ('b', 2)]


#Each element is a tuple.


# Access list

list_a = [1,2,3]

print(list_a[0])

print(list_a[-1])

#traverse
for num in list_a:
    print(num)

for i in range(len(list_a)):
    print(list_a[i])

# slicing

print(f"slicing {list_a[0:2]}")    

# Modification - Add elements
# 

list_a.append(4)    # default append at end

print(list_a)

# append at specific pos

list_a.insert(1,5)

print(list_a)


list_a.remove(4) # Removes first occurrence only.

print(list_a)

# delete by index or slice

del list_a[0]
del list_a[1:3]

# clear() → Remove all elements
print(list_a.index(5))

# count() → Count occurrences

# Sorting and Reversing

lst.sort()

lst.sort(reverse=True) # Descending

# sorted() → Returns new list

new_lst = sorted(lst)

# reverse()

#Other Useful Operations

len(lst)
max(lst)
min(lst)
sum(lst)


