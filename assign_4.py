import numpy as np

stock_prices = np.random.randint(10, 100, size=(30, 10))
print("Stock prices:\n", stock_prices)

closing_prices = stock_prices[:, -1]
print("Closing prices:\n", closing_prices)

max_closing_price = closing_prices.max()
print("Maximum closing price:\n", max_closing_price)

standard_deviation = np.std(closing_prices)
print("Standard deviation:\n", standard_deviation)
for i in range(0, 29):
    previous_day_price = (closing_prices[i] * 0.05) + closing_prices[i]
    if previous_day_price <= closing_prices[i + 1]:
        print("Day:", i + 2, "Price:", closing_prices[i + 1])
