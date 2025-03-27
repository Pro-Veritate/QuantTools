import matplotlib.pyplot as plt
class LN():
    def __init__(self, v=None, n=None):
        self.v = v
        self.n = n
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        plt.plot(range(len(prices)), prices, marker='o')
        plt.grid(True)
        time = 0
        active = False
        mins = []
        _ = len(prices)
        pr = None
        head = None
        for i in prices[::-1]:
            new_node = LN(i)
            new_node.n = head
            head = new_node
        prices = head
        av = prices.v
        while _>1 and av==prices.n.v:
            prices=prices.n
            _ -= 1
        if _>1 and av<prices.n.v:
            xc, yc = time, av
            mins.append(av)
            plt.text(xc, yc, 'B', color='red') #【买入】
        if prices.n!=None and prices.n.n!=None:
            active = True
            pr = prices.v
            prices=prices.n
            time += 1
        while prices.n!=None and prices.n.n!=None:
            av = prices.v
            while av==prices.n.v and prices.n!=None and prices.n.n!=None:
                prices = prices.n
                _ -= 1
            nt = prices.n.v
            if av<pr and av<nt:
                xc, yc = time, av
                mins.append(av)
                plt.text(xc, yc, 'B', color='red') #【买入】
            elif av>pr and av>nt:
                xc, yc = time, av
                plt.text(xc, yc, 'S', color='green') #【卖出】
            pr = av
            prices = prices.n
            time += 1
            active = True
        if prices.n!=None:
            av = prices.v
            nt = prices.n.v
            if av==nt:
                pass
            else:
                if active:
                    if av>pr and av>nt:
                        xc, yc = time, av
                        plt.text(xc, yc, 'S', color='green') #【卖出】
                    elif av<pr and av<nt:
                        xc, yc = time, av
                        plt.text(xc, yc, 'B', color='red') #【买入】
                        mins.append(av)
                if mins!=[] and av<nt:
                    time += 1
                    xc, yc = time, nt
                    plt.text(xc, yc, 'S', color='green') #【卖出】
        plt.show()
