import re
from collections import Counter

def clean(s):
    return re.sub(r'[^a-z]', '', s.lower())

def is_anagram(a, b):
    return Counter(clean(a)) == Counter(clean(b))

print(is_anagram("Dormitory", "Dirty room!!"))  # ✅ True
