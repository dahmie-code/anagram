# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    if(len(word) == len(anagram)):
        return True
    word = sorted(word)
    anagram = sorted(anagram)


word = "secure"
anagram="rescue"
print(find_anagram(word, anagram))