word = input("Text your word for check: ").lower()

word_reverse = word[::-1]

if word == word_reverse:
    print(f"Your word is palindrome: {word} - {word_reverse}")
else:
    print(f"Your word is not a palindrome: {word} - {word_reverse}")
