import string
x = string.punctuation

def is_palindrome(text):
    text = list(text.lower())
    text2_0 = list()
    for i in text:
        if i in x or i == ' ':
            pass
        else:
            text2_0.append(i)
    text3_0 = []
    b = -1
    for i in text2_0:
        text3_0.append(text2_0[b])
        b -= 1
    if text2_0 == text3_0:
        return True
    else:
        return False

text = input('Type text:')
is_palindrome(text)


