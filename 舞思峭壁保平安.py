import matplotlib.pyplot as plt
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_time, sell_time = 0, 0
        buy_price, sell_price = None, None
        mp = 0
        for time, price in enumerate(prices):
            if price<prices[buy_time]:
                buy_time, buy_price  = time, price # 更新买入
            if price - prices[buy_time]>mp:
                mp = price - prices[buy_time]
                sell_time, sell_price = time, price # 更新卖出
        if buy_price!=None and sell_price!=None:
            plt.text(buy_time, buy_price, 'B', color='red')
            plt.text(sell_time, sell_price, 'S', color='green')
        plt.grid(True)
        plt.plot(range(len(prices)), prices, marker='o')
        plt.show()
