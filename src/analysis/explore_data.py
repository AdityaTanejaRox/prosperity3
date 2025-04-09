import pandas as pd
from src.utils.data_loader import get_prices, get_trades

ROUND = 1
DAY = 0

def main():
    print("Loading data...")

    # Load prices
    prices = get_prices(ROUND, DAY)
    print(f"Prices loaded: {prices.shape}")
    print(prices.head())

    # Load trades
    trades = get_trades(ROUND, DAY)
    print(f"Trades loaded: {trades.shape}")
    print(trades.head())

    # Example: Group trades by product
    print("\nAverage trade prices per product:")
    avg_trade_prices = trades.groupby("product")["price"].mean()
    print(avg_trade_prices)

    # Example: Most traded products
    print("\nMost traded products:")
    print(trades["product"].value_counts())

if __name__ == "__main__":
    main()
