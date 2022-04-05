# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
letter = input('Please enter a letter from the alphabet (a-z or A-Z): ')
print(letter)
# 2. Write the code that determines whether the letter entered is a vowel
if(letter=='A' or letter=='a' or letter=='E' or letter =='e' or letter=='I'or letter=='i' or letter=='O' or letter=='o' or letter=='U' or letter=='u'):
  print(f'the letter {letter} is a vowel')
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant
else:
  print(f'the letter {letter} is a constanant')

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':