# creating a list

# num=[10,20,30,40]
# # print(num)

# num1=[10,10.5,"Python"]
# print(num1)

# accessing an element
# print(num[1])
# print(num1[-1])

#calculate length of list
# print(len(num))
# print(len(num1))


# traversing a list
# for i in num:
#   print(i)

# i=0
# while i<len(num1):
#   print(num1[i])
#   i+=1

# append a list
# num.append(100)
# print(num)

# added element on specific index
# num.insert(2,"python")
# print(num)

# #delete element
# num.remove(100)
# print(num)

#delete the element using pop()
# num.pop()
# print(num)

# # clearing a list
# num.clear()
# print(num) 


# Traversing a list from both sides 
# a=[10,20,30,40,50]
# print(a[1:4])
# print(a[::-1])

# merging two list
# a=[10,20,30,40,50,20.45,39.00]
# b=["DS","Python","React"]
# a.extend(b)
# print(a)

# occurence count - specific element
# a=[10,20,30,20,20,20,40,50]
# print(a.count(20))

# find index of element
# a=[10,20,"python",40,50]
# print(a.index('python'))
# print(a.index(50))


# sorting list
# a=[20,70,10,200,5]
# a.sort()
# print(a)

# a.sort(reverse=True)
# print(a)


# reverse a list
# a=[10,20,"python",50]
# a.reverse()
# print(a) 

# # copy list to other list
# a=[1,2,3,4,5,"python"]
# b=a.copy()
# print(b)

# # concate two list
# a=[1,2]
# b=[3,4]
# c=a+b
# print(c)

# check membership
# a=[10,20,30,40,50]
# print(20 in a)

#unique element
# b=[10,20,30,30,30,20,10,90]
# res=list(set(b))
# print(res)


#calculate sqaure of numbers from 1 to 5
res=[a*a for a in range(1,6)]
print(res)

res=[a*a for a in range(6)]
print(res)

# [1,4,9,16,25]

#calculate even numbers

even=[x for x in range(11)
      if x%2==0]
print(even)
