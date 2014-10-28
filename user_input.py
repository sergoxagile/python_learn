def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


somethng = input('Input text:')
if (is_palindrome(somethng)):
    print('Yes it\'s palindrom')
else:
    print('No it\s not')