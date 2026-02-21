numbers = []

while True:
    val = input("Enter numbers or type stop to stop: ")

    if val.lower()== "stop":
        break

    numbers.append(int(val)) 

total = 0
for i in numbers:
    total += i

avg = total / len(numbers)

print("Numbers are:", numbers)
print("Sum is:", total)
print("Average is:", avg)
