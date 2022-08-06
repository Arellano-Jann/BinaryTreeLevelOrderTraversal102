def maxProfit(self, prices: List[int]) -> int:
        sale, best = max(prices),0
        for x in prices:
            if x < sale: 
                sale = x
            price = x - sale
            if price > best: 
                best = price
        return best



def maxProfit2(self, prices: List[int]) -> int:
    best_price = 0
    sell_price = prices[-1] # last index bc it's the highest possible last value
    for x in prices[::-1]: # has to be backwards bc sell_price is the last val
            price = sell_price - x
            if price > best_price: # saves the best possible price by taking the max
                best_price = price
            if x > sell_price: # saves the lowest possible sale price taking advantage of the fact that we want the highest sale value and the sale value is at the end.
                sell_price = x
    return best_price