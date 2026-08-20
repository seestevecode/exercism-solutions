"""Find anagrams of a specified word from a list of candidates"""

def find_anagrams(word, candidates):
    return [
        candidate 
        for candidate in candidates 
        if sorted(candidate.lower()) == sorted(word.lower()) 
            and candidate.lower() != word.lower()
    ]
