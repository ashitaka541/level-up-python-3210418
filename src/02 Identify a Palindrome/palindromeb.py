import re


def is_palindrome(text):
    text = input()
    forwards = ''.join(re.findall(r'[a-z]', text.lower()))
    backwards = forwards[::-1]
    return forwards == backwards