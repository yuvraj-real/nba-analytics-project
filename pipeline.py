import pandas as pd
import sqlite3

def run_pipeline():
    print("Extracting data...")
    df = pd.read_csv('nba_dailyleaders_full.csv')
    
    print("Transforming data...")
    #cleans up the NaN values in some percentage columns
    df['3P%'] = df['3P%'].fillna(0.0)
    df['FT%'] = df['FT%'].fillna(0.0)
    df['FG%'] = df['FG%'].fillna(0.0)
    
    #calculates the eFG% (effective field goal percentage)
    df['eFG%'] = (df['FG'] + (0.5 * df['3P'])) / df['FGA']
    df['eFG%'] = df['eFG%'].fillna(0.0)
    
    print("Adding to Database...")
    #connect to database and pushes
    conn = sqlite3.connect('nba_stats.db')
    df.to_sql('player_logs', conn, if_exists='replace', index=False)
    conn.close()
    
    print("nba_stats.db is ready")

if __name__ == "__main__":
    run_pipeline()