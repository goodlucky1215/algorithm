import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        count = 0
        for s in stones:
            if s in freqs:
                freqs[s] +=1
            else:
                freqs[s]=1
        for s in jewels:
            if s in freqs:
                count+=freqs[s]
        return count

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0
        for s in stones:
            freqs[s] +=1

        for s in jewels:
            count+=freqs[s]
        return count

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0
        for s in jewels:
            count+=freqs[s]
        return count

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)