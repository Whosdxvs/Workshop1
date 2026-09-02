-- Dimension: Country
CREATE TABLE IF NOT EXISTS dim_country (
    country_sk INTEGER PRIMARY KEY,
    country_name TEXT NOT NULL
);

-- Dimension: Technology
CREATE TABLE IF NOT EXISTS dim_technology (
    technology_sk INTEGER PRIMARY KEY,
    technology_name TEXT NOT NULL
);

-- Dimension: Seniority
CREATE TABLE IF NOT EXISTS dim_seniority (
    seniority_sk INTEGER PRIMARY KEY,
    seniority_name TEXT NOT NULL
);

-- Dimension: Date
CREATE TABLE IF NOT EXISTS dim_date (
    date_sk INTEGER PRIMARY KEY,
    full_date TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    quarter INTEGER NOT NULL
);

-- Dimension: Candidate
CREATE TABLE IF NOT EXISTS dim_candidate (
    candidate_sk INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL
);

-- Fact: Application
CREATE TABLE IF NOT EXISTS fact_application (
    candidate_sk INTEGER,
    date_sk INTEGER,
    country_sk INTEGER,
    technology_sk INTEGER,
    seniority_sk INTEGER,
    yoe INTEGER,
    code_challenge_score INTEGER,
    technical_interview_score INTEGER,
    is_hired INTEGER,
    FOREIGN KEY (candidate_sk) REFERENCES dim_candidate (candidate_sk),
    FOREIGN KEY (date_sk) REFERENCES dim_date (date_sk),
    FOREIGN KEY (country_sk) REFERENCES dim_country (country_sk),
    FOREIGN KEY (technology_sk) REFERENCES dim_technology (technology_sk),
    FOREIGN KEY (seniority_sk) REFERENCES dim_seniority (seniority_sk)
);
