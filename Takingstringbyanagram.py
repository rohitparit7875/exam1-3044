# Q3 - Palindromic Anagram
from collections import Counter

def has_palindromic_anagram(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    count = Counter(s)
    odd_counts = sum(1 for v in count.values() if v % 2 == 1)
    return odd_counts <= 1

# Example
print(has_palindromic_anagram("carrace"))   # True (can make "racecar")
print(has_palindromic_anagram("aabbcc"))    # True
print(has_palindromic_anagram("abc"))       # False
print(has_palindromic_anagram("Tact Coa"))  # True ("taco cat")
