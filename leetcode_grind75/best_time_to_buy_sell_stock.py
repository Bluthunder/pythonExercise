"""
Date - 12 April 2024
Leetcode Grind 75 Question: 5

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


def max_profit(prices: list[int]) -> int:
    buy = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] - buy > profit:
            profit = prices[i] - buy

    return profit


if __name__ == '__main__':
    stock_prices = [10, 7, 88, 3, 6, 4]
    print(f'Maximum profit which can be earned in this transaction: '
          f'{max_profit(stock_prices)}')
