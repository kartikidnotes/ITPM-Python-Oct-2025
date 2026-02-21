# # created a blank tuple
# # t=()

# #creation of tuple
# # t=(10,20,30)
# # print(t)

# #accessing specific elements
# t=(100,200,300,400)
# print(t[0])
# print(t[-1])


# # error : since tuple is immutable we cannot update the values at runtime
# # t[0]=200
# # print(t)

# Calculate length of tuple
# t=(10,2,"python",20.3,"IT")
# print("Size of tuple is ",len(t))

# #trasverse the tuple 
# t=(10,2,"python",20.3,"IT")
# for i in t:
#     print(i)


# #checking membership in tuple 
# t=(10,2,"python",20.3,"IT")
# print(10 in t)

# tuple slicing
# t=(10,20,30,40,50)
# print(t[1:3])
# print(t[::-1])

# #tuple Concatenation using + operator 
# a=(10,20)
# b=(30,40)
# c=a+b
# print(c)


# count and index
# t=(120,30,40,10,10,10,10)
# print(t.count(10))
# print(t.index(10))

# # convert list - tuple

# lst=[10,20,30,40]
# t=tuple(lst)
# print(t)


# 10 20
# 30 40
#nested tuple
# t=((10,20),(30,40))
# for i in t:
#     for j in i:
#         print(j,end=" ")


#swap values 
# a,b=10,20
# print(a,b)
# a,b=b,a
# print(a,b)


# min and max -- tuple
t=(100,50,90)
print(max(t))
print(min(t))


