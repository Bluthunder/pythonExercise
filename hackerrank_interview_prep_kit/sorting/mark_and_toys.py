def maximumToys(prices, k):
    toys = total = 0
    prices.sort()

    for price in prices:
        total += price
        if total > k:
            break
        toys += 1
    return toys
