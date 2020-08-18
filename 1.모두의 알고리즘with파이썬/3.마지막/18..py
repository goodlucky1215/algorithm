def max_profit(price):
    max_p=0
    n=len(price)
    for i in range(0,n-1):
        for j in range(i,n):
            if max_p<price[j]-price[i]:
                max_p=price[j]-price[i]
    return max_p

stock=[10300,9600,9800,8200,7800,8300,9500,9800,10200,9500]
print(max_profit(stock))

def max_profit(price):
    max_p=0
    min_p=price[0]
    n=len(price)
    for i in range(1,n):
        p=price[i]-min_p
        if max_p<p:
            max_p=p
        if min_p>price[i]:
            min_p=price[i]
    return max_p

stock=[10300,9600,9800,8200,7800,8300,9500,9800,10200,9500]
print(max_profit(stock))
