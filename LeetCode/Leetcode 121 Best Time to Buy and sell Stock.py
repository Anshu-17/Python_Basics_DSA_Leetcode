prices = [7, 1, 5, 3, 6, 4, 8]

# Brute Force Approach
def maxProfit(prices):
    max_profit = 0
    n = len(prices)
    for i in range(n):
        for j in range(i+1,n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit

print(maxProfit(prices))

'''Time Complexity: O(n^2)
Space Complexity: O(1)'''

# Optimized Approach
def maxProfitOPtimized(prices):
    min_price = float("inf")
    max_profit = 0
    n = len(prices)
    for i in range(n):
        min_price = min(min_price,prices[i])
        max_profit = max(max_profit,prices[i]-min_price)
    return max_profit

print(maxProfitOPtimized(prices))

'''Time Complexity: O(n)
Space Complexity: O(1)'''