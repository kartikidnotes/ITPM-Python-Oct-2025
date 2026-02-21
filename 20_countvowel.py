str="Programming Lanaguage"
vowels="aeiou"
count=0

for ch in str:
    if ch in vowels:
        count=count+1

print(count)