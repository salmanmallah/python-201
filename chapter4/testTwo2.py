"""
    CHAPTER 4
    test 2.5
    test: * Define a function that take one word in string as input.
             * check that word if it is palindrom or not
             * and return Boleon value as True or false
"""


def is_palindrome(name):
    if name == name[::-1]:
        return True
    return False


print(is_palindrome('nalan'))
