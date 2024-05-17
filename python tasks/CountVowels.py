vowels=['a','e','i','o','u']
str=input('Enter string : ')
countOfVowels=0
for c in str:
    if c in vowels:
        countOfVowels+=1
print('No. of vowels',countOfVowels)