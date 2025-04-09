from strategies.strategy1 import Trader
from utils.logger import get_logger

# Initialize trader and logger
logger = get_logger("main")
trader = Trader()

def run_strategy(state):
    logger.info("Received new state")
    result = trader.run(state)
    logger.info(f"Returned result: {result}")
    return result

if __name__ == "__main__":
    # This is typically not run directly; the platform handles it.
    # But you can run local tests or mock state here.
    logger.info("Running main as script (for local testing)")
    sample_state = {}  # Replace this with a mock test state for debugging
    run_strategy(sample_state)
