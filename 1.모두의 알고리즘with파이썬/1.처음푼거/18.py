def max_profit(price):
    p=len(price)
    max_p=0
    for i in range(p-1):
        for j in range(i+1,p):
            if max_p<price[j]-price[i]:
                max_p=price[j]-price[i]

    return max_p

stock=[10300,9600,9800,8200,7800,8300,9500,9800,10200,9500]
print(max_profit(stock))
