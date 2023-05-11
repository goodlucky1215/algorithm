import collections
import queue
from typing import List
import collections
import re


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
paragraph = re.sub(r'[^a-z\s]','',paragraph)
print(paragraph)
paragraph_change=''
paragraph_change = paragraph_change.upper()
paragraph_list = paragraph_change.split()
paragraph_counter = collections.Counter(paragraph_list)
paragraph_most = paragraph_counter.most_common(len(paragraph_counter))
print(paragraph_counter)
for i in paragraph_most:
    print(i[0])