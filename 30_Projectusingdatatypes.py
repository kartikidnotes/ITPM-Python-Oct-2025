
# list will store the names of students - dupliacte 
students=[]
#courses -- set
courses=set() 

while True:
    print("============Student Management System==================")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Show COurses")
    print("5. Exit")

    choice=input("Enter Your Choice :")

    if choice=="1":
        sid=int(input("Enter your Id : "))
        name=input("Enter YOur Name : ")
        course=input("Enter course Name : ")
        marks=int(input("Enter Marks : "))
        student_id=(sid,)

        student={
            "id":student_id,
            "name":name,
            "course":course,
            "marks":marks
        }

        students.append(student)
        courses.add(course)
        print("Student added Sucessfully!!!!")

    elif choice=="2":
        if not students:
            print("No Student Data is Found!!!")
        else:
            for s in students:
                print("ID :",s["id"][0])
                print("Name :",s["name"]) 
                print("Course :",s["course"])
                print("Marks ",s["marks"])

    elif choice=="3":
        search_id=int(input("Enter Id to Search a Student : "))
        found=False

        for s in students:
            if s["id"][0]==search_id:
                print("Student Found!!!")
                print(s)
                found=True
                break
            if not found :
                print("Student NOt FOund!!!")

    elif choice=="4":
        print("Courses Are :")
        for c in courses:
            print(c)
        print()

    elif choice=="5":
        print("Thank YOu ")
        break

    else:
        print("Invalid Choice!! Please Try Again!!! ")