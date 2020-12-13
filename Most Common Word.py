#Given a paragraph and a list of banned words
#Return the most frequent word that is not in list of banned words

import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                    if word not in banned]

        Count = collections.Counter(words)

        return Count.most_common(1)[0][0]

OUTPUT = Solution()

print(OUTPUT.mostCommonWord(paragraph, banned))
