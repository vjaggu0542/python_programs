from unittest import result


def ispalindrome(s):
    return s==s[::-1]
result=ispalindrome("mom")
if result:
    print("this is a palindrome")
else:
    print("this is not a palindrome")