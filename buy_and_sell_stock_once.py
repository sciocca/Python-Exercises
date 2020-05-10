def buy_and_sell(open_market_price):
    highest_profit = 0
    for index1,i in enumerate(open_market_price):
        for index2,j in enumerate(open_market_price):
            if ( index1 > index2 ):
                if (i - j >= highest_profit):
                    highest_profit = i - j
    return highest_profit





print(buy_and_sell([310,315,275,295,260,270,290,230,255,250]))
#this should equal 30, buy at 260 and sell at 290


#book answer
def buy_and_sell_stock_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit

print(buy_and_sell_stock_once([310,315,275,295,260,270,290,230,255,250]))

