str="Blueberry Blast"
frq={}

for ch in str:
    frq[ch]=frq.get(ch,0)+1

    # dual functionality --> trasverese  + maintain the count

print(max(frq,key=frq.get)) 

# json--> key : value
# {rollno :1 , name :'raj',
#  rollno :2 , name :'ram'}