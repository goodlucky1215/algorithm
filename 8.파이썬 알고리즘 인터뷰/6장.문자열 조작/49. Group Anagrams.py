import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_group = collections.defaultdict(list)
        for anagram in strs:
            word_group[''.join(sorted(anagram))].append(anagram)
        return word_group.values()