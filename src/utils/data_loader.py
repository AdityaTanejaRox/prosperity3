import pandas as pd
from pathlib import Path

DATA_ROOT = Path(__file__).parent.parent.parent / "data"

def get_prices(round_num: int, day_num: int) -> pd.DataFrame:
    path = DATA_ROOT / f"round{round_num}" / f"prices_round_{round_num}_day_{day_num}.csv"
    return pd.read_csv(path, sep=";")

def get_trades(round_num: int, day_num: int) -> pd.DataFrame:
    for suffix in ["wn", "nn"]:
        path = DATA_ROOT / f"round{round_num}" / f"trades_round_{round_num}_day_{day_num}_{suffix}.csv"
        if path.is_file():
            return pd.read_csv(path, sep=";")
    raise FileNotFoundError(f"Trades file not found for round {round_num}, day {day_num}")
