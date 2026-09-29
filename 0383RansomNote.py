class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        smaller = {}
        for letter in ransomNote:
            if letter not in smaller:
                smaller[letter] = 1
            else:
                smaller[letter] += 1

        larger = {}
        for letter in magazine:
            if letter not in larger:
                larger[letter] = 1
            else:
                larger[letter] += 1
        
        for letter in smaller:
            if letter not in larger or larger[letter] < smaller[letter]:
                return False

        return True
