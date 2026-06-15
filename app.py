import streamlit as st
import pandas as pd
import sqlite3

st.title("NBA Player Analytics Dashboard")

# connects to the SQL database
conn = sqlite3.connect('nba_stats.db')

# gets a list of all players for the dropdown
players_df = pd.read_sql("SELECT DISTINCT Player FROM player_logs ORDER BY Player", conn)
selected_player = st.selectbox("Select a Player", players_df['Player'])

# queries the database for the selected player
query = f"SELECT Date, Opp, PTS, TRB, AST, GmSc FROM player_logs WHERE Player = '{selected_player}'"
player_data = pd.read_sql(query, conn)

st.subheader(f"Game Logs for {selected_player}")
st.dataframe(player_data)

st.subheader("Scoring Trend")
st.line_chart(player_data.set_index('Date')['PTS'])

conn.close()