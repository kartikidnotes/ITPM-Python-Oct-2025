# break : stop the loop / conditional statement immediately
#continue : continue your loop skip particular condition 

for i in range(1,11):
    if i==5:
        break
    print(i)


for i in range(1,11):
    if i==5:
        continue
    print(i)


# password check 

while True:
    pwd=input("Enter Password : ")
    if pwd=="admin":
        print("Access Granted!!! ")
        break