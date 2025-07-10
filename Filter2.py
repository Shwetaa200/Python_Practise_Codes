alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

def is_vowel(letter):
    vowels = {'A', 'E', 'I', 'O', 'U'}  # Use a set for faster lookup
    return letter in vowels  # Check if the letter is in the vowel set

filtered_obj = filter(is_vowel, alphabet)
print(list(filtered_obj))  # Output: ['A', 'E', 'I']
