#가장싸게 사서 나중에 가장 비싸게 파는 주식찾기

#방법1: 모두 비교하기
def max_profit(prices):
    n = len(prices)
    max_profit=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if max_profit < prices[j]-prices[i]:
                max_profit=prices[j]-prices[i]

    return max_profit

stock=[10300,9600,9800,8200,7800,8300,9500,9800,10200,9500]
print(max_profit(stock))

#방법2: 한 번 반복
def max_profit(prices):
    n = len(prices)
    max_profit=0
    min_prices = prices[0]
    for i in range(1,n):
        profit = prices[i]-min_prices
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_prices:
            min_prices = prices[i]
            
    return max_profit

stock=[10300,9600,9800,8200,7800,8300,9500,9800,10200,9500]
print(max_profit(stock))
