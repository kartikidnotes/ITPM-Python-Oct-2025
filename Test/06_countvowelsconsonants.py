s=input("Enter String :  ")
vowels=0
consonants=0

for ch in s:
    if('a'<=ch <='z') or ('A'<=ch<='Z'):
        if ch in "aeiouAEIOU":
            vowels+=1
        else:
            consonants+=1

print("Vowel Count is : ",vowels)
print("Consonant Count is : ",consonants)
