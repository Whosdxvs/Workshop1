import pandas as pd

def extract_data(filepath: str) -> pd.DataFrame:
    """
    Extracts the source data from a CSV file.
    """
    print(f"Extracting data from {filepath}...")
    df = pd.read_csv(filepath, sep=';')
    print(f"Extracted {len(df)} records.")
    return df
