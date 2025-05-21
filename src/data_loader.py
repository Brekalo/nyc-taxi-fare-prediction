
import pandas as pd

def load_taxi_data(file_path: str) -> pd.DataFrame:
    """
    Loads NYC taxi fare dataset from CSV file.

    Args:
        file_path (str): Path to the CSV file

    Returns:
        pd.DataFrame: Loaded dataset
    """
    df = pd.read_csv(
        file_path,
        na_values=["", " ", "NA", "N/A", "null", "NULL"]
    )
    print(f"Dataset loaded from {file_path}. Shape: {df.shape}")
    return df
