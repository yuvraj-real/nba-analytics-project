# NBA Player Analytics: End-to-End ETL Pipeline
**[Live Interactive Dashboard Here](https://nba-analytics-project.streamlit.app/)**

## 📋 Project Overview
This Data Engineering project creates an automated pipeline that extracts basketball performance data from the 25-26 NBA season, transforms it to correct missing values and add a new metric for eFG%, and then load it into a relational database. The data is accessible from a live interactive web dashboard.

The goal of this project was to practice and demonstrate proficiency in Python, SQL, data cleaning, and systems architecture.

## System Architecture (ETL)

1. Extract: Gets data from CSV dataset containing over 28,000 individual NBA game logs.
2. Transform (Python/Pandas): Cleans missing numerical data (null percentage handling) and created a new metric column, the effective field goal percentage (eFG%), that better weighs in three pointers compared to the normal field goal percentage
3. Load (SQLite): Established a local database connection and converted the in-memory pandas DataFrame into a structured, queryable SQL table (player_logs).
4. Web Dashboard (Streamlit): A website that dynamically queries the SQLite database based on user inputs to render live analytical charts for scoring trends.

## Development
- Language: Python
- Data Manipulation: Pandas
- Database Engine: SQLite3
- Visualization: Streamlit
- Deployment: Git, GitHub, Streamlit Community Cloud


## SQL Analytics
- Besides the dashboard, I created various SQL queries to look at more insights from the database.

- For example, here is the query to find the:

Best Individual Performances by Points in Losses
SELECT 
    Player, 
    Tm, 
    Date, 
    PTS, 
    TRB, 
    AST, 
    GmSc 
FROM player_logs
WHERE Result = 'L'
GROUP BY Date
ORDER BY PTS DESC
LIMIT 10;


## How to Run Locally

If you want to run the pipeline and database on your own machine:

1. Clone the repository:

   git clone https://github.com/yuvraj-real/nba-analytics-project
   cd nba-analytics-pipeline

2. Intall required files:

    pip install -r requirements.txt

3. Execute the pipeline:

    python pipeline.py

4. Launch Dashboard:

    streamlit run app.py


