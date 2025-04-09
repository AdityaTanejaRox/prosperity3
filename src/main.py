from algorithms.strategy1 import Trader
from utils.logger import setup_logger

# Initialize trader and logger
logger = setup_logger("main")
trader = Trader()

def run_strategy(state):
    logger.info("Received new state")
    result = trader.run(state)
    logger.info(f"Returned result: {result}")
    return result

if __name__ == "__main__":
    # This is typically not run this way for IMC; the platform runs it.
    # But you can run backtests or mocks here if needed.
    logger.info("Running main as script (for local testing)")
    sample_state = {}  # Replace this with mock or test state
    run_strategy(sample_state)
