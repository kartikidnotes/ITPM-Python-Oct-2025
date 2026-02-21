m1=float(input("Enter First Subject Marks :"))
m2=float(input("Enter Second Subject Marks :"))
m3=float(input("Enter Third Subject Marks :"))

per=(m1+m2+m3)/3
print("Per is :",per)

if per>90:
    print("Grade A")
elif per>75:
    print("Grade B")
elif per>55:
    print("Grade C")
elif per>35:
    print("Grade D")
else:
    print("Fail")
