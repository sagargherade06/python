def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    return vowel_count, consonant_count

# Input validation loop
while True:
    text = input("Enter a string (only letters): ")
    if text.isalpha():  # Check if the input only contains letters
        break
    else:
        print("Invalid input. Please enter only alphabetic characters.")

# Count vowels and consonants
vowels, consonants = count_vowels_consonants(text)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
