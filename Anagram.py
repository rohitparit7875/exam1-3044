# Q1 - Check Anagram
from collections import Counter

def is_anagram(a, b):
    a = ''.join(ch.lower() for ch in a if ch.isalnum())
    b = ''.join(ch.lower() for ch in b if ch.isalnum())
    return Counter(a) == Counter(b)

# Example
print(is_anagram("Listen", "Silent"))   # True
print(is_anagram("Hello", "Olelh"))
