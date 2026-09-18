print("Stock Portfolio Tracker")
print("-----------------------")

stock_prices = {
    "AAPL": 180,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180,
    "TSLA": 250
}

portfolio = {}

while True:
    stock = input("Enter stock symbol: ").upper()

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        continue

    portfolio[stock] = quantity

    total = stock_prices[stock] * quantity

    print("Stock:", stock)
    print("Quantity:", quantity)
    print("Total Investment: $", total)

    again = input("Do you want to add another stock? (yes/no): ").lower()

    if again == "no":
        break

print("\nYour Portfolio:")
print("----------------")

for stock, quantity in portfolio.items():
    print(stock, "-", quantity, "shares")

total_portfolio_value = 0

for stock, quantity in portfolio.items():
    total_portfolio_value += stock_prices[stock] * quantity

print("Total Portfolio Value: $", total_portfolio_value)
