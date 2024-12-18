#count vowels and consonants in string
''''str='chandrakant'
vowels='aeiou'
vowels_count=0
consonants_count=0
for i in str:
    if i in vowels:
        vowels_count+=1
    else:
        consonants_count+=1
    
print("no of vowels",vowels_count)
print('no of consonants',vowels_count) '''''

def vowels_count(text):
    vowels='aeiouAEIOU'
    vowels_count1=0
    consonants_count=0
    for i in text:
        if i.isalpha():
            if i in vowels:
                vowels_count1+=1
            else:
                consonants_count+=1
    return vowels_count1,consonants_count
text=str(input("enter the string"))
vowels_count1,consonants_count=vowels_count(text)
print(vowels_count1)
print(consonants_count)