# creating a set
# s={10,20,30}
# print(s)

# add element in set
# s={1,2}
# s.add(300)
# print(s)

# #remove
# s={1,2,300}
# s.remove(300)
# print(s)

# #discard
# s={1,2,300}
# s.discard(300)
# print(s)

#traversing a set
# since set dont have indexing it will not print in order
# s={10,20,30,40}
# for i in s:
#     print(i)

# union
# a={10,20}
# b={30,40,50,60,10,20}
# print(a | b)

# #intersection
# a={10,20}
# b={30,40,50,60,10,20}
# print(a & b)


#difference
# a={1,2}
# b={2,3}
# print(a-b)
# print(b-a)

# # symmetric difference
# a={1,2}
# b={2,3}
# print(a^b)

# #set membership
# s={10,20}
# print(20 in s)

# remove duplicates in set
lst=[10,20,30,20,20,20]
res=list(set(lst))
print(res)

# subset and superset
a={10,20}
b={10,20,30}
print(a.issubset(b))
print(b.issuperset(a))

# common elements between two list
a=[10,20,30]
b=[10,20,30,40,50,60]
print(list(set(a) & set(b)))
