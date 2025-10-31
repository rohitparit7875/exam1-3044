# 1) Simple / readable: check if two strings are anagrams (ignores spaces & case)
def is_anagram_sorted(a: str, b: str) -> bool:
    a_clean = ''.join(a.lower().split())
    b_clean = ''.join(b.lower().split())
    return sorted(a_clean) == sorted(b_clean)

# Example
print(is_anagram_sorted("Listen", "Silent"))   # True
print(is_anagram_sorted("Dormitory", "Dirty room"))  # True
