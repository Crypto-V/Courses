def check_palindrome(value):
    x = ''
    for i in range(len(value)):
        x += word[len(value) - 1 - i]
    return x


word = input('give me a word:\n')
x = check_palindrome(word)
if x == word:
    print('This is a Palindrome')
else:
    print('This is NOT a Palindrome')
