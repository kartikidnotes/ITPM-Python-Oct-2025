# check whether an email Id is valid or not 
# @ end -->.in / .com / .org

str="ram123@tcs.in"

if "@" in str and str.endswith(".in"):
    print("Valid Email")
elif "@" in str and str.endswith(".com"):
    print("Valid Email")
elif "@" in str and str.endswith(".org"):
    print("Valid Email")
else:
    print("Invalid Email")

