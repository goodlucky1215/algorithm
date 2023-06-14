class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_price = prices[0]
        for i in prices:
            if min_price<i:
                result = max(result,i-min_price)
            else :
                min_price=i
        return  result

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_price = prices[0]
        for i in prices:
            result = max(result,i-min_price)
            min_price= min(min_price, i)
        return  result