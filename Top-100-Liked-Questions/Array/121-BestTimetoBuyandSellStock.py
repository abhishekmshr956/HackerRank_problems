def besttime_naive(prices):
    """ naive solution """
    n = len(prices)
    profits = [0] * n
    for i in range(n-1):
        profits[i] = max(max(prices[i+1:]) - prices[i], 0)
    return max(profits)

def besttime_naive1(prices):
    n = len(prices)
    max_profit = 0
    for i in range(n-1):
        for j in range(i+1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

def besttime(prices):
    # l = 0
    # r = 0
    # max_profit = 0
    # for r in range(1, len(prices)):
    #     if prices[r] < prices[l]:
    #         l = r
    #         r = l + 1
    #     elif prices[r] > prices[l]:
    #         profit = prices[r] - prices[l]
    #         if profit > max_profit:
    #             max_profit = profit
    #         r += 1
    # return max_profit

    """ optimal solution """
    l, r = 0, 1 # l = buy, r = sell
    max_profit = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    return max_profit

    

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    # prices = [7,6,4,3,1]
    # prices = [1,2]
    print(besttime_naive(prices))
    print(besttime_naive1(prices))
    print(besttime(prices))