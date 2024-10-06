"""
    You are given two strings sentence1 and sentence2, each representing a sentence composed of words. 
    A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
    Each word consists of only uppercase and lowercase English characters.
    Two sentences s1 and s2 are considered similar if it is possible to insert 
    an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. 
    Note that the inserted sentence must be separated from existing words by spaces.
"""

def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    words1 = sentence1.split()
    words2 = sentence2.split()

    # Ensure that words1 is always the shorter or equal length sentence
    if len(words1) > len(words2):
        words1, words2 = words2, words1

    i = 0
    # Check for common prefix
    while i < len(words1) and words1[i] == words2[i]:
        i += 1

    # Check for common suffix
    j = 0
    while j < len(words1) - i and words1[-(j+1)] == words2[-(j+1)]:
        j += 1

    # If all words of the shorter sentence were checked
    return i + j == len(words1)

sentence1 = "Hello Jane"
sentence2 = "Hello my name is Jane"
print(areSentencesSimilar(sentence1, sentence2))
