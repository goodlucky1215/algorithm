import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph_change = paragraph.lower()
        paragraph_change = re.sub(r'[^a-z\s]',' ',paragraph_change)
        paragraph_list = paragraph_change.split()
        paragraph_counter = collections.Counter(paragraph_list)
        paragraph_most_word = paragraph_counter.most_common(len(paragraph_counter))
        for i in paragraph_most_word:
            if i[0] not in banned :
                return  i[0]