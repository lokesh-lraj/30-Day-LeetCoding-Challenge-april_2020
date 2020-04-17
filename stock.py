def maxProfit(self, prices: List[int]) -> int:
        with_stock = -2147483647
        without_stock = 0
        for stock in prices :
            with_stock = max(with_stock, without_stock - stock)
            without_stock = max(without_stock, with_stock + stock)
        return without_stock
