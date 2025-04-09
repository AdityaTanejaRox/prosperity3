from src.strategies.datamodel import OrderDepth, TradingState, Order
from typing import List, Dict, Tuple
from src.utils.logger import get_logger

logger = get_logger("strategy1")

class Trader:
    
    def run(self, state: TradingState) -> Tuple[Dict[str, List[Order]], int, str]:
        logger.info("Trader data: %s", state.traderData)
        logger.info("Observations: %s", str(state.observations))

        result = {}
        for product in state.order_depths:
            order_depth: OrderDepth = state.order_depths[product]
            orders: List[Order] = []
            acceptable_price = 10  # Placeholder logic
            logger.info(f"{product} - Acceptable price: {acceptable_price}")
            logger.info(f"{product} - Buy depth: {len(order_depth.buy_orders)}, Sell depth: {len(order_depth.sell_orders)}")

            # Buy logic
            if order_depth.sell_orders:
                best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
                if int(best_ask) < acceptable_price:
                    logger.info(f"{product} - BUY {-best_ask_amount} @ {best_ask}")
                    orders.append(Order(product, best_ask, -best_ask_amount))

            # Sell logic
            if order_depth.buy_orders:
                best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
                if int(best_bid) > acceptable_price:
                    logger.info(f"{product} - SELL {best_bid_amount} @ {best_bid}")
                    orders.append(Order(product, best_bid, -best_bid_amount))

            result[product] = orders

        traderData = "SAMPLE"
        conversions = 1  # Set to 0 if no conversion required

        logger.info(f"Final result: {result}, conversions: {conversions}, traderData: {traderData}")
        return result, conversions, traderData
