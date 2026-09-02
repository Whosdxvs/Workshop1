import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the source data by applying business rules and standardizations.
    """
    print("Transforming data...")
    # Make a copy to avoid SettingWithCopyWarning
    transformed_df = df.copy()

    # 1. Standardizing column names (removing spaces, lowercase)
    transformed_df.columns = [col.strip().lower().replace(' ', '_') for col in transformed_df.columns]
    
    # Ensure application_date is datetime
    transformed_df['application_date'] = pd.to_datetime(transformed_df['application_date'])

    # 2. Implement the hiring business rule
    # HIRED = (Code Challenge Score >= 7) AND (Technical Interview Score >= 7)
    transformed_df['is_hired'] = (
        (transformed_df['code_challenge_score'] >= 7) & 
        (transformed_df['technical_interview_score'] >= 7)
    ).astype(int)
    
    print(f"Transformation complete. Data shape: {transformed_df.shape}")
    return transformed_df
