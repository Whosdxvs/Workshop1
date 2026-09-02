import pandas as pd
from typing import Dict

def build_dimensional_model(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """
    Transforms the prepared source data into dimensional structures (Star Schema).
    """
    print("Building dimensional model...")
    
    # 1. DimCountry
    dim_country = pd.DataFrame({'country_name': df['country'].unique()}).reset_index(drop=True)
    dim_country.insert(0, 'country_sk', dim_country.index + 1)
    
    # 2. DimTechnology
    dim_tech = pd.DataFrame({'technology_name': df['technology'].unique()}).reset_index(drop=True)
    dim_tech.insert(0, 'technology_sk', dim_tech.index + 1)
    
    # 3. DimSeniority
    dim_seniority = pd.DataFrame({'seniority_name': df['seniority'].unique()}).reset_index(drop=True)
    dim_seniority.insert(0, 'seniority_sk', dim_seniority.index + 1)
    
    # 4. DimDate
    unique_dates = df['application_date'].dt.date.unique()
    dim_date = pd.DataFrame({'date': pd.to_datetime(unique_dates)}).sort_values('date').reset_index(drop=True)
    dim_date.insert(0, 'date_sk', dim_date.index + 1)
    dim_date['full_date'] = dim_date['date'].dt.strftime('%Y-%m-%d')
    dim_date['year'] = dim_date['date'].dt.year
    dim_date['month'] = dim_date['date'].dt.month
    dim_date['day'] = dim_date['date'].dt.day
    dim_date['quarter'] = dim_date['date'].dt.quarter
    # Drop 'date' to only keep standard types if desired, but 'full_date' works
    dim_date = dim_date.drop(columns=['date'])
    
    # 5. DimCandidate
    # Assuming the combination of first_name, last_name, and email is unique for a candidate.
    candidate_cols = ['first_name', 'last_name', 'email']
    dim_candidate = df[candidate_cols].drop_duplicates().reset_index(drop=True)
    dim_candidate.insert(0, 'candidate_sk', dim_candidate.index + 1)
    
    # 6. FactApplication
    # Map surrogate keys
    fact_df = df.copy()
    
    # Map Country
    fact_df = fact_df.merge(dim_country, left_on='country', right_on='country_name', how='left')
    # Map Technology
    fact_df = fact_df.merge(dim_tech, left_on='technology', right_on='technology_name', how='left')
    # Map Seniority
    fact_df = fact_df.merge(dim_seniority, left_on='seniority', right_on='seniority_name', how='left')
    # Map Candidate
    fact_df = fact_df.merge(dim_candidate, on=['first_name', 'last_name', 'email'], how='left')
    # Map Date
    fact_df['date_str'] = fact_df['application_date'].dt.strftime('%Y-%m-%d')
    fact_df = fact_df.merge(dim_date, left_on='date_str', right_on='full_date', how='left')
    
    # Select Fact Columns
    fact_application = fact_df[[
        'candidate_sk', 
        'date_sk', 
        'country_sk', 
        'technology_sk', 
        'seniority_sk', 
        'yoe', 
        'code_challenge_score', 
        'technical_interview_score', 
        'is_hired'
    ]]
    
    print("Dimensional model built successfully.")
    
    return {
        'dim_country': dim_country,
        'dim_technology': dim_tech,
        'dim_seniority': dim_seniority,
        'dim_date': dim_date,
        'dim_candidate': dim_candidate,
        'fact_application': fact_application
    }
