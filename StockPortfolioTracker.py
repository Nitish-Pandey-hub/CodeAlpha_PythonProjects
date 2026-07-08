stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}


def get_investment_details():
    portfolio = {}
    
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Enter stock name and quantity. Type 'done' to finish.\n")
    
    while True:
        stock = input("Stock name (or 'done'): ").upper().strip()
        
        if stock == "DONE":
            break
        
        if stock not in stock_prices:
            print(f"'{stock}' not found in price list. Try again.")
            continue
        
        try:
            quantity = int(input(f"Quantity of {stock}: "))
            if quantity < 0:
                print("Quantity can't be negative.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    
    return portfolio


def calculate_total(portfolio):
    total = 0
    breakdown = []
    
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total += value
        breakdown.append((stock, qty, price, value))
    
    return breakdown, total


def display_summary(breakdown, total):
    print("\n--- Investment Summary ---")
    print(f"{'Stock':<8}{'Qty':<6}{'Price':<10}{'Value':<10}")
    for stock, qty, price, value in breakdown:
        print(f"{stock:<8}{qty:<6}{price:<10}{value:<10}")
    print(f"\nTotal Investment: ${total:,.2f}")


def save_to_file(breakdown, total, filename="investment_summary.txt"):
    with open(filename, "w") as f:
        f.write("Stock,Quantity,Price,Value\n")
        for stock, qty, price, value in breakdown:
            f.write(f"{stock},{qty},{price},{value}\n")
        f.write(f"\nTotal Investment,,,{total:.2f}\n")
    print(f"Summary saved to {filename}")


def main():
    portfolio = get_investment_details()
    
    if not portfolio:
        print("No stocks entered. Exiting.")
        return
    
    breakdown, total = calculate_total(portfolio)
    display_summary(breakdown, total)
    
    save = input("\nSave summary to file? (y/n): ").lower().strip()
    if save == "y":
        save_to_file(breakdown, total)


if __name__ == "__main__":
    main()