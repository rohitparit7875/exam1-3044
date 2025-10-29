# Q2 - Check Palindrome
def is_palindrome(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]

# Example
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("No lemon, no melon"))              # True
print(is_palindrome("Hello"))                           # False
