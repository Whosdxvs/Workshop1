-- R1 - Hiring Trends
-- Monitor hiring trends over time to identify changes in recruitment outcomes.
-- Query: Monthly hiring trends
SELECT 
    d.year, 
    d.month, 
    COUNT(f.candidate_sk) AS total_applications,
    SUM(f.is_hired) AS total_hires,
    ROUND(SUM(f.is_hired) * 100.0 / COUNT(f.candidate_sk), 2) AS hire_rate_percentage
FROM fact_application f
JOIN dim_date d ON f.date_sk = d.date_sk
GROUP BY d.year, d.month
ORDER BY d.year, d.month;


-- R2 - Technology Analysis
-- Compare hiring results across technologies.
-- Query: Hiring performance by technology
SELECT 
    t.technology_name,
    COUNT(f.candidate_sk) AS total_applications,
    SUM(f.is_hired) AS total_hires,
    ROUND(SUM(f.is_hired) * 100.0 / COUNT(f.candidate_sk), 2) AS hire_rate_percentage
FROM fact_application f
JOIN dim_technology t ON f.technology_sk = t.technology_sk
GROUP BY t.technology_name
ORDER BY total_hires DESC;


-- R3 - Candidate Profile Analysis
-- Analyze hiring outcomes according to candidate seniority and years of experience.
-- Query: Hiring rate by seniority and average years of experience of hired candidates
SELECT 
    s.seniority_name,
    COUNT(f.candidate_sk) AS total_applications,
    SUM(f.is_hired) AS total_hires,
    ROUND(AVG(f.yoe), 1) AS avg_yoe_all_candidates,
    ROUND(AVG(CASE WHEN f.is_hired = 1 THEN f.yoe ELSE NULL END), 1) AS avg_yoe_hired_candidates,
    ROUND(SUM(f.is_hired) * 100.0 / COUNT(f.candidate_sk), 2) AS hire_rate_percentage
FROM fact_application f
JOIN dim_seniority s ON f.seniority_sk = s.seniority_sk
GROUP BY s.seniority_name
ORDER BY hire_rate_percentage DESC;


-- R4 - Geographic Recruitment Analysis
-- Identify countries with the highest recruitment activity and compare their hiring outcomes.
-- Query: Top 10 countries by application volume and their hiring outcomes
SELECT 
    c.country_name,
    COUNT(f.candidate_sk) AS total_applications,
    SUM(f.is_hired) AS total_hires,
    ROUND(SUM(f.is_hired) * 100.0 / COUNT(f.candidate_sk), 2) AS hire_rate_percentage
FROM fact_application f
JOIN dim_country c ON f.country_sk = c.country_sk
GROUP BY c.country_name
ORDER BY total_applications DESC
LIMIT 10;


-- R5 - Assessment Performance Analysis
-- Analyze the relationship between Code Challenge and Technical Interview scores by Seniority
-- Query: Average scores across seniority levels for all candidates vs hired candidates
SELECT 
    s.seniority_name,
    ROUND(AVG(f.code_challenge_score), 2) AS avg_code_challenge_all,
    ROUND(AVG(f.technical_interview_score), 2) AS avg_tech_interview_all,
    ROUND(AVG(CASE WHEN f.is_hired = 1 THEN f.code_challenge_score ELSE NULL END), 2) AS avg_code_challenge_hired,
    ROUND(AVG(CASE WHEN f.is_hired = 1 THEN f.technical_interview_score ELSE NULL END), 2) AS avg_tech_interview_hired
FROM fact_application f
JOIN dim_seniority s ON f.seniority_sk = s.seniority_sk
GROUP BY s.seniority_name
ORDER BY avg_code_challenge_all DESC;
