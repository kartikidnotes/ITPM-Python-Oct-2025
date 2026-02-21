# #create tuple
# num=(10,20,30,40,50)
# print("Tuple is :",num)
# print("First element of tuple is :",num[0])
# print("Last element of tuple is :",num[-1])
# print("Length of tuple is :",len(num))

# #prove that tuple is immutable
# colors=("red","yellow","green","green","green")
# print("Tuple is :",colors)
# print("Occurence of Green color is :",colors.count("green"))
# colors[0]="blue"

marks=[10,20,30,60,80,9,8,0]
marks.append(1)
marks.insert(2,200)
print(marks)

marks.sort()
print(marks)

for i in marks:
    print(i)


A={10,20,30}
B={30,40,50,10,20}

print("Union is :",A|B)
print("Intersection is :",A&B)
print("Difference is :",B-A)
