
import pandas as pd

def preprocess_taxi_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies preprocessing to raw NYC taxi fare dataset.

    Args:
        df (pd.DataFrame): Raw dataset

    Returns:
        pd.DataFrame: Cleaned dataset
    """
    # Drop rows with missing values
    df = df.dropna()

    # Additional processing steps can go here (datetime conversion, feature engineering, etc.)
    # For example:
    if 'tpep_pickup_datetime' in df.columns:
        df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])

    return df
