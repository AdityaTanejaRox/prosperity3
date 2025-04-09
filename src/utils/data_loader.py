import pandas as pd
import os

def load_market_data(file_name, data_dir='data'):
    """
    Load market data from a CSV file into a DataFrame.
    """
    file_path = os.path.join(data_dir, file_name)
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"{file_path} does not exist.")
