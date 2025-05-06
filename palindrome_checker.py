''' Palindrome checker '''

word = input("Enter a word: ")

# Remove spaces and make lowercase (optional)
cleaned = word.replace(" ", "").lower()

# Check if the word is the same forwards and backwards
if cleaned == cleaned[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
