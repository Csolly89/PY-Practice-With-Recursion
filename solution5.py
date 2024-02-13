def is_palindrome(str):
    if len(str) == 1 or len(str) == 0:
        return True
    else:
        return (str[0] == str[-1]) and is_palindrome(str[1:-1])

print("is 'Gandalf' a palindrome?")
print(is_palindrome('Gandalf'))
print("is 'rotator' a palindrome?")
print(is_palindrome('rotator'))