import sqlite3
import pandas as pd
from typing import Dict

def load_data(dimensional_model: Dict[str, pd.DataFrame], db_path: str):
    """
    Loads the dimension and fact tables into the SQLite Data Warehouse.
    """
    print(f"Loading data into {db_path}...")
    
    # Connect to the SQLite database (this will create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    
    try:
        # Load Dimensions first
        dimensional_model['dim_country'].to_sql('dim_country', conn, if_exists='replace', index=False)
        dimensional_model['dim_technology'].to_sql('dim_technology', conn, if_exists='replace', index=False)
        dimensional_model['dim_seniority'].to_sql('dim_seniority', conn, if_exists='replace', index=False)
        dimensional_model['dim_date'].to_sql('dim_date', conn, if_exists='replace', index=False)
        dimensional_model['dim_candidate'].to_sql('dim_candidate', conn, if_exists='replace', index=False)
        
        # Load Fact Table
        dimensional_model['fact_application'].to_sql('fact_application', conn, if_exists='replace', index=False)
        
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Error loading data: {e}")
    finally:
        conn.close()
