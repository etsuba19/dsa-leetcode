import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        separated = paragraph.split()

        counts = {}
        words = re.split(r"[ !?',;.]+", paragraph)
        print(words)
        for word in words:
            if not word:
                continue

            word = word.lower()

            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
        
        # print(counts)
        theKey = ""
        maxnum = 0

        for key, value in counts.items():
            if key in banned:
                continue
            if value > maxnum:
                maxnum = value
                theKey = key
        
        return theKey
