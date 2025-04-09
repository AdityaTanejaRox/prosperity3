from datamodel import OrderDepth, TradingState, Order
from typing import List, Dict, Tuple

class Trader:
    def __init__(self):
        # Initialize a dictionary to keep track of the number of orders per product
        self.order_counts = {product: 0 for product in ['RAINFOREST_RESIN', 'SQUID_INK', 'KELP']}

    def run(self, state: TradingState) -> Tuple[Dict[str, List[Order]], int, str]:
        result = {}
        for product in state.order_depths:
            order_depth = state.order_depths[product]
            orders = []
            acceptable_price = 10  # Replace with dynamic logic

            # Check if the product has already hit its limit
            if self.order_counts[product] < 50:
                if order_depth.sell_orders:
                    best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
                    if best_ask < acceptable_price:
                        # Calculate new potential order count
                        new_order_count = self.order_counts[product] + abs(best_ask_amount)
                        if new_order_count <= 50:
                            orders.append(Order(product, best_ask, -best_ask_amount))
                            self.order_counts[product] = new_order_count  # Update the order count

                if order_depth.buy_orders:
                    best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
                    if best_bid > acceptable_price:
                        # Calculate new potential order count
                        new_order_count = self.order_counts[product] + abs(best_bid_amount)
                        if new_order_count <= 50:
                            orders.append(Order(product, best_bid, -best_bid_amount))
                            self.order_counts[product] = new_order_count  # Update the order count

            result[product] = orders

        traderData = "SAMPLE"
        conversions = 0
        return result, conversions, traderData
