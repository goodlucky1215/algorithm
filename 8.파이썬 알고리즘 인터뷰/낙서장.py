import collections
import queue
from typing import List
import collections
import re


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
paragraph = re.sub(r'[^\w]',' ',paragraph)
print(paragraph)
paragraph_change = paragraph.upper()
paragraph_list = paragraph_change.split()
paragraph_counter = collections.Counter(paragraph_list)
paragraph_most = paragraph_counter.most_common(len(paragraph_counter))
print(paragraph_counter.most_common(1)[0])
print(paragraph_most)
