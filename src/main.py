import os
from extract import extract_data
from transform import transform_data
from dimensional_model import build_dimensional_model
from load import load_data

def main():
    print("Starting ETL Process...")
    
    # Define paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    source_path = os.path.join(base_dir, 'data', 'raw', 'candidates.csv')
    db_path = os.path.join(base_dir, 'database', 'recruitment_dw.db')
    
    # 1. Extract
    df_raw = extract_data(source_path)
    
    # 2. Transform
    df_transformed = transform_data(df_raw)
    
    # 3. Dimensional Model
    dimensional_data = build_dimensional_model(df_transformed)
    
    # 4. Load
    load_data(dimensional_data, db_path)
    
    print("ETL Process completed successfully.")

if __name__ == "__main__":
    main()
