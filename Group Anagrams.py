#Given an array of strings 'strs', group the anagrams together
#You can return answer in any order

import collections

Input = ["eat", "tea", "tan", "ate", "nat", "bat"]

class Solution:
    def groupAnagrams(self, strs):
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()

OUTPUT = Solution()

print(OUTPUT.groupAnagrams(Input))
